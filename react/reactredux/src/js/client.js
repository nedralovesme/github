import React from "react";
import ReactDOM from "react-dom";
import TodoApp from "./components/TodoApp";
import { Provider,connect } from "react-redux";
import store from "./store";

//AJAX library
import axios from "axios";
//import reducer from "./reducers"; //should get the export default
const app = document.getElementById('app');


store.dispatch({type:"ADD_TODO",payload:{text:"something"}});
store.dispatch({type:"ADD_TODO",payload:{text:"something else"}});

store.dispatch((dispatch) => {
        dispatch({type:"ADD_TODO",payload:{text:"#3"}});
        //async here
        axios.get("https://jsonplaceholder.typicode.com/posts")
            .then((response) => {
                console.log(response);
                dispatch({type:"ADD_TODO",payload:{text:"#4"}});
            })
            .catch((err) => {
                //dispatch error
            });
        //done with async
})
ReactDOM.render(<Provider store={store}><TodoApp /></Provider>, app);
