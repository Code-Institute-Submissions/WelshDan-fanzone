import React from "react";
import NoResults from "../assets/ref-red.jpg";
import styles from "../styles/NotFound.module.css";
import Asset from "./Asset";

const NotFound = () => {
  return (
    <div className={styles.NotFound}>
      <Asset
        message={`Sorry, the page you're looking for doesn't exist.`}
        src={NoResults}

      />
    </div>
  );
};

export default NotFound;
