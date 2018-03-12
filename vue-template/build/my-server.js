const express = require('express')
const webpack = require('webpack')

const webpackConfig = require('./webpack.dev.conf')
const webpackMiddleware = require("webpack-dev-middleware");
var compiler = webpack(webpackConfig)
var app = express()
app.use(webpackMiddleware(compiler, {serverSideRender: true}))


app.get('/school',function (req, res) {
  res.send(`
  
  
   
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    
    <body>
    <div id="app"></div>
  
    <script type="text/javascript" src="school.js"></script>
    
    </body>
    </html>
    
    
  
  `)
})


app.listen(6060)


