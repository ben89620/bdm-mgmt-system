<template>
  <div>
    <h2>Excel 清單資料</h2>
    <table border="1">
      <thead>
        <tr>
          <th v-for="(val, key) in items[0]" :key="key">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in items" :key="i">
          <td v-for="(val, key) in row" :key="key">{{ val }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const items = ref([])

onMounted(async () => {
  const res = await axios.get('http://localhost:5000/list')
  items.value = res.data
})
</script>
