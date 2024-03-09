/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      screens :{
        'max-md' : {'max': '1024px'},
        'max-lg' : {'min': '1024px'},
      },
    },
  },
  plugins: [],
}