const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            cart: [],
            premium: true
        }
    },
    methods: {
        updateCart(id) {
            this.cart.push(id)
        }
    }
})
