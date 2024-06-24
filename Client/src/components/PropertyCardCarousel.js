import React from 'react';
import Slider from 'react-slick';
import '../pages/css/PropertyCardCarousel.css';

const PropertyCardCarousel = ({propertyCards}) => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  };

  return (
    <div className="carousel-container">
      <Slider {...settings}>
        {propertyCards}
      </Slider>
    </div>
  );
};

export default PropertyCardCarousel;
