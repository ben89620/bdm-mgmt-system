<template>
  <div class="login-container">
    <form @submit.prevent="handleLogin" class="login-form">
      <h2>登入</h2>
      <div class="form-group">
        <label>帳號</label>
        <input 
          type="text" 
          v-model="username" 
          required 
          placeholder="請輸入帳號"
        >
      </div>
      <div class="form-group">
        <label>密碼</label>
        <input 
          type="password" 
          v-model="password" 
          required 
          placeholder="請輸入密碼"
        >
      </div>
      <button type="submit" :disabled="isLoading">
        {{ isLoading ? '登入中...' : '登入' }}
      </button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits(['login-success'])

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  try {
    const response = await axios.post('http://localhost:8000/login', {
      username: username.value,
      password: password.value
    })
    
    if (response.data.status === 'success') {
      emit('login-success')
    }
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || '登入失敗'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}

.login-form {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 300px;
}

.form-group {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
