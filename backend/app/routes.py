from flask import Blueprint, request, jsonify
from .db import get_db_connection

main = Blueprint('main', __name__)

@main.route('/')
def hello():
    return "Flask + MySQL 接好了！"

# ✅ 新增定存資料 API（POST）
@main.route('/api/fixed_deposits', methods=['POST'])
def add_fixed_deposit():
    data = request.json
    currency = data.get('currency')
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO FixedDeposits (user_id, currency, amount, interest_rate, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (1, currency, amount, interest_rate, start_date, end_date))  # user_id 暫時固定為 1

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "定存資料新增成功 ✅"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
