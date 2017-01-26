var React = require('react')
var ReactDOM = require('react-dom')

var Post = React.createClass ({
    render: function() {
        return (
          <h1>{this.props.name}</h1>
        )
    }
})

ReactDOM.render(<Post />, document.getElementById('container'))
