const path = require("path");

module.exports = {
  entry: "./calculator/scr/",
  output: {
    path: path.resolve(__dirname, "calculator/static"),
    filename: "main.js",
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        test: /\.(ts|tsx)$/,
        use: {
          loader: "ts-loader",
        },
      },
    ],
  },
  // pass all js files through Babel
  resolve: {
    extensions: [".*", ".js", ".jsx", ".ts", ".tsx"], // <-- added `.jsx` here
  },
};