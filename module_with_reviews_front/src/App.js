import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [factories, setFactories] = useState([]);
  const [selectedFactory, setSelectedFactory] = useState(null);
  const [rating, setRating] = useState(1);
  const [feedback, setFeedback] = useState('');
  const [status, setStatus] = useState('Отлично');
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/factories')
      .then(response => setFactories(response.data))
      .catch(error => console.error(error));
  }, []);

  useEffect(() => {
    if (selectedFactory) {
      axios.get(`http://localhost:8000/reviews/${selectedFactory.id}/`)
        .then(response => setReviews(response.data))
        .catch(error => console.error(error));
    }
  }, [selectedFactory]);

  const handleFactorySelect = (factory) => {
    setSelectedFactory(factory);
  };

  const handleReviewSubmit = () => {
    if (!selectedFactory) return;
    const newReview = { rating, feedback, status };
    axios.post(`http://localhost:8000/factories/${selectedFactory.id}/reviews`, newReview)
      .then(response => {
        console.log(response.data);
        axios.get(`http://localhost:8000/reviews/${selectedFactory.id}/`)
          .then(response => setReviews(response.data))
          .catch(error => console.error(error));

                setRating(1);
        setFeedback('');
        setStatus('Отлично');
      })
      .catch(error => console.error(error));
  };

  const renderStatusIcon = () => {
    switch (status) {
      case 'Отлично':
        return '😀';
      case 'Нормально':
        return '🙂';
      case 'Плохо':
        return '☹️';
      default:
        return null;
    }
  };


  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"></link>
      <h1>Factories</h1>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {factories.map(factory => (
          <li
            key={factory.id}
            style={{
              cursor: 'pointer',
              padding: '10px',
              margin: '5px',
              border: '1px solid #ddd',
              borderRadius: '5px',
              backgroundColor: selectedFactory && selectedFactory.id === factory.id ? '#eee' : 'inherit',
            }}
            onClick={() => handleFactorySelect(factory)}
          >
            {factory.name}
          </li>
        ))}
      </ul>
      {selectedFactory && (
        <div style={{ marginTop: '20px', border: '1px solid #ddd', padding: '15px', borderRadius: '5px' }}>



          <div style={{ marginTop: '20px', border: '1px solid #ddd', padding: '15px', borderRadius: '5px' }}>
          <h2>{selectedFactory.name}</h2>
          <p><strong>Адрес:</strong> {selectedFactory.address}</p>
          <h3>Отзыв</h3>
          <div style={{ marginBottom: '10px' }}>
            <label><strong>Рейтинг (от 1 до 5): </strong></label>
            <input type="number" value={rating} onChange={(e) => setRating(e.target.value)} min="1" max="5" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg"/>
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label><strong>Отзыв: </strong></label>
            <textarea value={feedback} onChange={(e) => setFeedback(e.target.value)} class="form-control" id="exampleFormControlTextarea1" />
          </div>


          <div style={{ marginTop: '10px' }}>
            <label><strong>Статус: </strong></label>
            <select value={status} onChange={(e) => setStatus(e.target.value)}  class="form-select form-select-sm" aria-label=".form-select-sm example">
              <option value="Отлично">Отлично</option>
              <option value="Нормально">Нормально</option>
              <option value="Плохо">Плохо</option>
            </select>
            {/* Display the selected icon */}
            <p style={{ fontSize: '100px' }}>{renderStatusIcon()}</p>
          </div>


          <button onClick={handleReviewSubmit} style={{ padding: '8px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
            Отправить отзыв
          </button>
        </div>



        <br></br>
        <br></br>
        <br></br>

        <h2>{selectedFactory.name}</h2>
          <p><strong>Адрес:</strong> {selectedFactory.address}</p>
          <h3>Отзывы: </h3>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            {reviews.map(review => (
              <li key={review.id} style={{ marginBottom: '10px' }}>
                <p><strong>Рейтинг:</strong> {review.rating}</p>
                <p><strong>Оценка:</strong> {review.status}</p>
                <p><strong>Отзыв:</strong> {review.feedback}</p>
              <br></br>
              </li>
            ))}
          </ul>


          
        </div>


      )}
    </div>
  );
}

export default App;
