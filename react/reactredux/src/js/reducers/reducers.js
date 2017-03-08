import { combineReducers } from "redux";
import userReducer from "./UserReducer";
import todoReducer from "./TodoReducer";
export default combineReducers({
    user:userReducer,todos:todoReducer
});
