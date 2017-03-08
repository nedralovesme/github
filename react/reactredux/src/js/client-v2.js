import React from "react";
import ReactDOM from "react-dom";
import { createStore, combineReducers } from "redux";
import TodoApp from "./components/TodoApp";
const app = document.getElementById('app');
//state is the current state
//action must have a type, and any value for payload
const todoReducer = function(state={todos:[]},action){
    var newState = Object.assign(state);
    //action.type is required!
    if(action.type=="ADD_TODO"){
        console.log(action);
        var todos = state.todos.concat(action.payload.text);
        newState = { ...state, todos:todos };
    }
    return newState; //returns the new value of the state
}

const userReducer = function(state={user:{}},action){
    switch(action.type) {
        case "CHANGE_NAME": {
            state = {...state, name:action.payload};
            break;
        }
    }
    return state;//must return the state
}

const reducers = combineReducers({
    user:userReducer,todos:todoReducer
});

//second argument is the starting state
const store = createStore(reducers, {});
store.subscribe(()=> {
        console.log("store changed:");
        console.log(store.getState());
    }
);
store.dispatch({type:"ADD_TODO",payload:{text:"something"}});
store.dispatch({type:"ADD_TODO",payload:{text:"something else"}});
ReactDOM.render(<TodoApp />, app);
