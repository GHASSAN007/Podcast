import React, { Component } from "react";
import loginPage from "./loginPage";

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,

} from "react-router-dom"


export default class HomePage extends Component {
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path="/"> <p>this is the HomePage</p> </Route>
                    <Route path="/login" Component={loginPage} />
                </Switch>
            </Router>
        )
    }
}

