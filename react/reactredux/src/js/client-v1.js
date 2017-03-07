import React from "react";
import ReactDOM from "react-dom";
import { createStore } from "redux";
import TodoApp from "./components/TodoApp";
const app = document.getElementById('app');
//state is the current state
//action must have a type, and any value for payload
const reducer = function(state,action){
    var newState = state;
    //action.type is required!
    if(action.type=="ADD_TODO"){
        var todos = state.todos.concat(action.payload.text);
        newState = { ...state, todos:todos };
    }
    return newState; //returns the new value of the state
}
//second argument is the starting state
const store = createStore(reducer, {todos:[]});
store.subscribe(()=> {
        console.log("store changed:");
        console.log(store.getState());
    }
);
store.dispatch({type:"ADD_TODO",payload:{text:"something"}});
store.dispatch({type:"ADD_TODO",payload:{text:"something else"}});
ReactDOM.render(<TodoApp />, app);
