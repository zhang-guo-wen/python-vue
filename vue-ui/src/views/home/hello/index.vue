<template>
  <div>
    myname is {{ name }}
    <el-button @click="getname"></el-button>
  </div>
</template>

<script>
import {hello} from "@/api/home/hello";

export default {
  name: "Home",
  data() {
    return {
      name: ""
    }
  },
  methods: {
    getname() {
      hello().then((res) => {
        this.name = res.data
      })
    }
  }
}
</script>

<style scoped>

</style>
