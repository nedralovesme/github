import { createStore,applyMiddleware } from "redux";
import reducers from "./reducers/reducers";
//plugin middleware
import logger from "redux-logger";

//read https://www.npmjs.com/package/redux-thunk
//allows you to delay actions
import thunk from "redux-thunk";
//TODO move store here:
//second argument is the starting state

//export it
export default createStore(reducers, {},applyMiddleware(thunk, logger()));
