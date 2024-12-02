/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Inclure vos templates Django
    "./static/**/*.js",
    "./static/**/*.css",
    "./**/admin/**/*.html", // Inclure les templates d'administration
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
