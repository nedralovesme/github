import React from "react";
import ReactDOM from "react-dom";
import { applyMiddleware,createStore, combineReducers } from "redux";
import TodoApp from "./components/TodoApp";

//plugin middleware
import logger from "redux-logger";

//read https://www.npmjs.com/package/redux-thunk
//allows you to delay actions
import thunk from "redux-thunk";

//AJAX library
import axios from "axios";
//import reducer from "./reducers"; //should get the export default
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
const store = createStore(reducers, {},applyMiddleware(thunk, logger()));
store.subscribe(()=> {
        console.log("store changed:");
        console.log(store.getState());
    }
);

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
ReactDOM.render(<TodoApp />, app);
