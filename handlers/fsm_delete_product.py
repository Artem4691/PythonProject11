from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers import buttons
from database import db


class DeleteProduct(StatesGroup):
    confirm = State()


router_delete_product = Router()


@router_delete_product.callback_query(F.data.startswith("delete:"))
async def delete_start(call: CallbackQuery, state: FSMContext):
    product_id = call.data.split(':')[1]
    await state.update_data(product_id=product_id)

    await call.message.answer(
        f'Вы уверены, что хотите удалить товар с артикулом {product_id}?',
        reply_markup=buttons.confirm_delete
    )
    await call.answer()
    await state.set_state(DeleteProduct.confirm)


@router_delete_product.callback_query(DeleteProduct.confirm, F.data == "confirm_delete_yes")
async def delete_confirm_yes(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_id = data['product_id']

    await db.delete_product_db(product_id=product_id)
    await call.message.answer(f"🗑 Товар (артикул {product_id}) успешно удалён!")
    await call.answer()
    await state.clear()


@router_delete_product.callback_query(DeleteProduct.confirm, F.data == "confirm_delete_no")
async def delete_confirm_no(call: CallbackQuery, state: FSMContext):
    await call.message.answer("❌ Удаление отменено.")
    await call.answer()
    await state.clear()
