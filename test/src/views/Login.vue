<template>
  <div>
    <h2>登入</h2>
    <input v-model="username" placeholder="帳號" />
    <input v-model="password" type="password" placeholder="密碼" />
    <button @click="login">登入</button>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const message = ref('')
const router = useRouter()


function login() {
  if (username.value === 'admin' && password.value === 'password') {
    router.push('/list')  // 登入成功，前往 list 頁面
  } else {
    errorMessage.value = '帳號或密碼錯誤'
  }
}
</script>
