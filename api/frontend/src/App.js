import React, { Component } from 'react';
import axios from 'axios'; // new


class App extends Component {
    state = {
        book: []
};

// new
componentDidMount() {
    this.getBook();
}

// new
getBook() {
    axios
        .get('http://127.0.0.1:8000/api/books/')
        .then(res => {
        this.setState({ book: res.data });
        })
        .catch(err => {
        console.log(err);
});
}

render() {
    return (
        <div>
            {this.state.book.map(item => (
                <div key={item.id}>
                    <h1>{item.title}</h1>
                    <span>{item.subtitle}</span>;&nbsp;
                    <span>{item.author}</span>;&nbsp;
                    <span>{item.isbn}</span>;&nbsp;
                </div>
            ))}
        </div>
    );
    }
}
export default App;