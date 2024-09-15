/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./apecs/**/templates/**/*.html'],
    theme: {
        extend: {
            colors: {
                'blue': '#074F8D',
                'orange': '#F26A24',
            },
        },
    },
    plugins: [],
}
