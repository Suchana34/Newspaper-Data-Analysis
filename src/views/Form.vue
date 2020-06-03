<template>
<div>
  <Navbar />
  <v-app id="inspire">
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          cols="12"
          sm="8"
          md="4"
        >
          <v-card class="elevation-12" shaped>
            <v-toolbar
              color="grey"
              flat
            >
              <v-toolbar-title><span class="font-weight-light" >Enter the URL of the Newspaper Article</span></v-toolbar-title>
              
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  label="URL"
                  name="url"
                  prepend-icon="mdi-link"
                  type="text"
                  color="grey"
                  v-model="url"
                  :rules="rules"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>

            <v-row justify="center">  <v-btn color="grey"><span class="font-weight-light" @click="getURL">Turn In</span></v-btn></v-row>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
  <Footer />
  </div>
</template>

<script>
  import Footer from '@/components/Footer.vue'
  import Navbar from '@/components/Navbar.vue'
  import axios from 'axios'
  import router from '../router/index'
  
  export default {
    name: 'Login',
    data: ()=>({
        url : '',
        rules: [
        value => !!value || 'Required.',
        value => (value || '').length >= 5 || 'Min 5 characters',
        
      ],
    }),
    methods:{
      
      getURL() {
      console.log('u r in');
      const path = 'http://127.0.0.1:5000/';
      axios.post(path, {url:this.url})
        // eslint-disable-next-line no-unused-vars
        .then(res => {
          router.push({ name: 'Result' })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    },
    components: {
      Footer,
      Navbar
    }
  }
</script>
