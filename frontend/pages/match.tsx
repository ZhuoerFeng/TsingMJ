import React from 'react';
import Link from 'next/link';
import styles from './match.module.css'; 

// Hardcoded list of items, replace this with your data
const listItems: string[] = ['半决赛桌I第一半庄', '半决赛桌I第二半庄', '半决赛桌J第一半庄', '半决赛桌J第二半庄'];
const nameItems: string[] = ['semi-I-1', 'semi-I-2', 'semi-J-1', 'semi-J-2']

const MatchPage: React.FC = () => (
  <div className={styles.container}>
    <ul className={styles.list}>
      {listItems.map((item, index) => (
        <li key={index} className={styles.listItem}>
          <Link href={`/display/${nameItems[index]}`} passHref>
            <button className={styles.button}> 
              {item}
            </button>
          </Link>
        </li>
      ))}
    </ul>
  </div>
)

export default MatchPage;