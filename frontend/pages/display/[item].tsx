import { useRouter } from 'next/router'
import React, { use, useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import {CategoryScale} from 'chart.js'; 
Chart.register(CategoryScale);


const DisplayItem: React.FC = () => {
    const router = useRouter();
    function transposeArray(array: any[][]): any[][] {
        if (!array) {
            return [];
        }
        let transposedArray: any[][] = [];
    
        // Assuming inner arrays have a fixed length of 4
        for (let i = 0; i < 4; i++) {
            let tempArray: any[] = [];
            for (let j = 0; j < array.length; j++) {
                tempArray.push(array[j][i]);
            }
            transposedArray.push(tempArray);
        }
    
        return transposedArray;
    }

    const [item, setItem] = useState<string | null>(null);

    useEffect(() => {
        if (router.isReady) {
            console.log(router.query);
            setItem(router.query.item as string);
        }
    }, [router.isReady]);

    const [scores, setScores] = useState<any[]>([]);
    const [players, setPlayers] = useState<string[]>([]);

    useEffect(() => {  
        const fetchData = async () => {
            if (item) {
                const response = await fetch(`http://localhost:8000/api/v1/paipu/name=${item}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                    }
                }); // Use your API url here
                const data = await response.json();
                console.log(data);
                setScores(data.score_list); // Use your data structure here
                setPlayers(data.name);
            }
        };

        fetchData();
        
    }, [item]);

    const data = transposeArray(scores);
    
    if (item == null) {
        return <div>Loading...</div>;
    }
    else if (scores == null) {
        return <div> 对局 : {item} Not Found  </div>
    }
  return (
    <>
        <div>
            <h2> 对局 : {item}</h2>
        </div>
        <Line
            data={{
                labels: scores.map((_, index) => index + 1),
                datasets: [
                {
                    label: players[0] || 'Player 1',
                    data: data[0] || [],
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                },
                {
                    label: players[1] || 'Player 2',
                    data: data[1] || [],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                },
                {
                    label: players[2] || 'Player 3',
                    data: data[2] || [],
                    borderColor: 'rgba(255, 206, 86, 1)',
                    backgroundColor: 'rgba(255, 206, 86, 0.2)',
                },
                {
                    label: players[3] || 'Player 4',
                    data: data[3] || [],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                },
                ],
            }}
        />
    </>
  );
}

export default DisplayItem;


