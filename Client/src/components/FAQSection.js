// src/components/FAQSection.js
import React, { useState } from 'react';
import '../pages/css/FAQSection.css';

const faqData = [
  {
    id: '1',
    question: 'How do I search for properties?',
    answer: 'You can use our search filters to find properties by location, price range, type, etc.',
  },
  {
    id: '2',
    question: 'Can I list my property on DreamNest?',
    answer: 'Yes, you can list your property by creating an account and filling out the property details.',
  },
  {
    id: '3',
    question: 'What payment methods do you accept?',
    answer: 'We accept major credit cards, PayPal, and bank transfers for transactions.',
  },
];

const FAQSection = () => {
  const [activeIndex, setActiveIndex] = useState(null);

  const toggleAccordion = (index) => {
    if (activeIndex === index) {
      setActiveIndex(null);
    } else {
      setActiveIndex(index);
    }
  };

  return (
    <section className="faq-section">
      <h2 className='faq-header'>FAQ</h2>
      <div className="faq-list">
        {faqData.map((faq, index) => (
          <div key={faq.id} className="faq-item">
            <div className="faq-question" onClick={() => toggleAccordion(index)}>
              <h3>{faq.question}</h3>
              <span className={`arrow ${activeIndex === index ? 'arrow-up' : 'arrow-down'}`}></span>
            </div>
            {activeIndex === index && (
              <div className="faq-answer">
                <p>{faq.answer}</p>
              </div>
            )}
          </div>
        ))}
      </div>
    </section>
  );
};

export default FAQSection;
