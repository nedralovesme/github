//returns from function will be info that is dispatched
//import in target file with
//import * as user from "/path/to/actions/userAction.js";
//call user.readUser
// OR
//import { readUser } from "/path/to/actions/userAction.js";
//call setUserName('Janice');

export function readUser(){
    console.log("reading a user");
    return {
        type:"READ_USER",
        payload:{name:"Bob",age:68},
    }
}

export function setUserName(name){
    return {
        type:"SET_USER_NAME",
        payload:name
    }
}
