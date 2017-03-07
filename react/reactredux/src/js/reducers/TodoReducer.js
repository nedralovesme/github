//state is the current state
//action must have a type, and any value for payload
export default function(state={todos:[]},action){
    var newState = Object.assign(state);
    //action.type is required!
    if(action.type=="ADD_TODO"){
        console.log(action);
        var todos = state.todos.concat(action.payload.text);
        newState = { ...state, todos:todos };
    }
    return newState; //returns the new value of the state
}
