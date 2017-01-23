var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: {
      // Add as many entry points as you have container-react-components here
      App1: './reactjs/App1',
      vendors: ['react'],
    },
    output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name]-[hash].js',
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
          compress: {
              warnings: false
          }
      }),
      //tells webpack where to store data about your bundles.
      new BundleTracker({filename: './webpack-stats.json'}),
      new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
      //makes jQuery available in every module
      new webpack.ProvidePlugin({
          $: 'jquery',
          jQuery: 'jquery',
          'window.jQuery': 'jquery'
      })
  ],
  module: {
    loaders: [
      {test: /\.jsx?$/,
        //we definitely don't want babel to transpile all the files in
        //node_modules. That would take a long time.
        exclude: /node_modules/,
        //use the babel loader
        loader: 'babel-loader',
        query: {
            //specify that we will be dealing with React code
            presets: ['react']
        }
      }
    ]
  },
  resolve: {
    //tells webpack where to look for modules
    modulesDirectories: ['node_modules'],
    //extensions that should be used to resolve modules
    extensions: ['', '.js', '.jsx']
  }
}
