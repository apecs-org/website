/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./apecs/**/templates/**/*.html'],
    theme: {
        extend: {
            colors: {
                'apecs-blue': '#074F8D',
                'apecs-orange': '#F26A24',
                'polarin-blue': '#0078FD',
            },
        },
    },
    plugins: [],
}
