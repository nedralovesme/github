import React from "react";
import TodoList from "./TodoList";
//import { connect } from "react-redux";
//import * as user from "../actions/userActions";

// user.readUser();
// @connect((store)=>{
//     //the return becomes props
//     return {
//         user:store.user
//     }
// })
export default class TodoApp extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {items: [], text: ''};
  }

  // componentWillMount(){
  //     console.log("Mounting:",this.props.user);
  //     this.props.dispatch(user.readUser());
  // }

  render() {
    return (
      <div>
        <h3>TODO</h3>

        <TodoList items={this.state.items} />
        <form onSubmit={this.handleSubmit}>
          <input onChange={this.handleChange} value={this.state.text} />
          <button>{'Add #' + (this.state.items.length + 1)}</button>
        </form>

      </div>
    );
    //<button onClick={user.readUser}>Read User</button>
  }

  handleChange(e) {
    this.setState({text: e.target.value});
  }

  handleSubmit(e) {
    e.preventDefault();
    var newItem = {
      text: this.state.text,
      id: Date.now()
    };
    this.setState((prevState) => ({
      items: prevState.items.concat(newItem),
      text: ''
    }));
  }
}
