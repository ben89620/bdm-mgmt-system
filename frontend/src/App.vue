<template>
  <div>
    <LoginForm v-if="!isLoggedIn" @login-success="handleLoginSuccess" />
    <div v-else>
      <h1>Excel 數據展示</h1>
      <button @click="logout" class="logout-btn">登出</button>
      <table>
        <thead>
          <tr>
            <th v-for="header in headers" :key="header">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in data" :key="index">
            <td v-for="header in headers" :key="header">{{ row[header] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import LoginForm from './components/LoginForm.vue'

const data = ref([])
const headers = ref([])
const isLoggedIn = ref(false)

const handleLoginSuccess = () => {
  isLoggedIn.value = true
  fetchExcelData()
}

const logout = () => {
  isLoggedIn.value = false
}

const fetchExcelData = async () => {
  try {
    const response = await axios.get('http://localhost:8000/excel')
    data.value = response.data
    headers.value = Object.keys(data.value[0] || {})
  } catch (error) {
    console.error('Error fetching data:', error.response ? error.response.data : error.message)
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

.logout-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
