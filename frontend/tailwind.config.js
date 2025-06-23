/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
    "./modules/products/**/*.{html,ts}" // Include your library
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
