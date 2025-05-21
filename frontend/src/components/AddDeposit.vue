<template>
  <div class="form-card">
    <h2>新增定存資料</h2>
    <form @submit.prevent="submitDeposit">
      <label>幣別：</label>
      <input v-model="form.currency" placeholder="例如 TWD" required />

      <label>金額：</label>
      <input type="number" v-model.number="form.amount" required />

      <label>年利率 (%)：</label>
      <input type="number" step="0.01" v-model.number="form.interest_rate" required />

      <label>開始日期：</label>
      <input type="date" v-model="form.start_date" required />

      <label>結束日期：</label>
      <input type="date" v-model="form.end_date" required />

      <button type="submit">新增定存</button>
    </form>

    <p v-if="message" style="margin-top: 1rem; color: green;">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AddDeposit',
  data() {
    return {
      form: {
        currency: '',
        amount: null,
        interest_rate: null,
        start_date: '',
        end_date: '',
      },
      message: ''
    }
  },
  methods: {
  async submitDeposit() {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/fixed_deposits', this.form)
      this.message = response.data.message
      this.form = { currency: '', amount: null, interest_rate: null, start_date: '', end_date: '' }
    } catch (error) {
      console.error('❌ 錯誤內容：', error.response || error.message)
      this.message = '發生錯誤，請稍後再試'
    }
  }
}
}
</script>

<style scoped>
.form-card {
  max-width: 400px;
  margin: auto;
  padding: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 12px;
  background: #f9f9f9;
  color: #222;
}
input, button {
  display: block;
  margin-top: 0.5rem;
  padding: 0.5rem;
  width: 100%;
}
button {
  background-color: #4caf50;
  color: white;
  border: none;
  margin-top: 1rem;
  cursor: pointer;
}
</style>
