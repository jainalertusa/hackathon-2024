import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import '../pages/css/HousePriceChart.css';

// Register necessary components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const HousePriceChart = ({filteredData, years }) => {
 console.log(filteredData, years)
  const chartData = {
    labels: years,
    datasets: [
      {
        label: filteredData.state,
        data: filteredData.prices,
        borderColor: '#8c6a43', // Brown
        backgroundColor: 'rgba(140, 106, 67, 1)', // Adjusted brown shade
        fill: false,
        lineTension: 0.5,
        animate:true
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: false,
        position: 'bottom',
      },
      title: {
        position:'bottom',
        display: true,
        text: 'House Prices Over Years',
      },
      tooltip: {
        mode: 'index',
        intersect: false,
      },
      hover: {
        mode: 'nearest',
        intersect: true,
      },
    },
    scales: {
      x: {
        display: false,
        title: {
          display: true,
          text: 'Years',
        },
      },
      y: {
        display: false,
        title: {
          display: true,
          text: 'Prices in Dollars',
        },
      },
    },
  };

  return (
    <Line data={chartData} options={options} />
  );
};

export default HousePriceChart;
