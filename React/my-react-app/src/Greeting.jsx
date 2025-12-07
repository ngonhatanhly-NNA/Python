import React from "react";
// Functional Components
function Greet(props) {
    return <h1>Hello, {props.name}!</h1>;
}
// Class Components
class Greet extends React.Component{
    render(){
        return <h1>Hello, {this.props.name}1</h1>;
    }
}