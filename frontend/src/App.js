import React, { useEffect, useState } from 'react';
import getList from './services/list.js'


function App() {
  const [list, setList] = useState([]);

  useEffect(() => {
    let mounted = true;
    getList()
      .then(items => {
        if(mounted) {
          setList(items.results)
          console.log(items.results)
        }
      })
    return () => mounted = false;
  }, [])

  return (
    <div className="App">
      Hacklights!
      <ul>
       {list.map(item => <li key={item.pub_date}>{item.title} - {item.url} by {item.author}</li>)}
     </ul>
    </div>
  );
}

export default App;
