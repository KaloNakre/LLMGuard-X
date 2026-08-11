/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0a0a0a",
        foreground: "#ededed",
        primary: "#3b82f6",
        danger: "#ef4444",
        success: "#22c55e",
        warning: "#f59e0b"
      },
    },
  },
  plugins: [],
};
