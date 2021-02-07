CREATE PROCEDURE InitDB ()
    RETURNS NULL
    AS {LANGUAGE plpgsql;
    CREATE TABLE Maps (
        id integer NOT NULL UNIQUE,
        TableName varchar(40 ) NOT NULL UNIQUE,
    );
    };
    --LANGUAGE plpgsql;
    --create new table Map, and add it name to
CREATE PROCEDURE create_new_map (mapname text ) RETURNS NULL AS
{ LANGUAGE plpgsql;
    CREATE TABLE $ mapname (
    Chunkid integer NOT NULL UNIQUE,
    ChunkData int[32][32][32],
    code char(5) CONSTRAINT firstkey PRIMARY KEY,
    title varchar(40) NOT NULL,
    date_prod date,
    kind varchar(10),
    len interval hour TO minute
);
RETURNS 0;
};

--LANGUAGE plpgsql;
;

