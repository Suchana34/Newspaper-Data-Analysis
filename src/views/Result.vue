<template>
  <div>
    <Navbar />
    <v-app id="result">
      <v-row align = "center" justify="center"> 
        <v-simple-table height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-center">Props</th>
                <th class="text-center">Result</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{ props }}</td>
                <td>{{ result }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-row>
    </v-app>
    
  <Footer />

  </div>
</template>

<script>
import axios from 'axios';
import Footer from '@/components/Footer.vue'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Result',
  components:{
    Navbar,
    Footer
  },
  data: () => ({
      props: 'Article Author',
      result: '' 
  }),
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/';
      axios.get(path)
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
}
</script>