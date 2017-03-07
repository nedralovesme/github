import React from "react";

export default class Timer extends React.Component {
    //Custom constructor
    constructor(props) {
        //Call the parent component's constructor
        super(props);
        //set initial state with a custom property
        this.state = {
            secondsElapsed: 0
        };
    }

    //custom function to increment the internal state
    tick() {
        //update the state, take prevState as an input parameter
        //set current state.secondsElapsed to prevState.secondsElapsed + 1
        this.setState((prevState) => ({
            secondsElapsed: prevState.secondsElapsed + 1
        }));
    }

    //start the timer on mounting
    componentDidMount() {
        this.interval = setInterval(() => this.tick(), 1000);
    }

    //stop the timer
    componentWillUnmount() {
        clearInterval(this.interval);
    }

    //draws the component
    render() {
        return ( <div> Seconds Elapsed: {
                this.state.secondsElapsed
            } < /div>
        );
    }
}
