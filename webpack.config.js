const path = require('path')
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: './apecs/static/src/index.js',
    output: {
        path: path.resolve(__dirname, 'apecs/static/dist'),
        filename: 'tailwind.js',
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                include: path.resolve(__dirname, 'apecs/static/src'),
                use: ['style-loader', 'css-loader', 'postcss-loader'],
            },
        ],
    },
    plugins: [
        new CopyWebpackPlugin({
            patterns: [
                {from: path.resolve(__dirname, 'apecs/static/src/htmx.min.js')}
            ]
        })
    ]
}