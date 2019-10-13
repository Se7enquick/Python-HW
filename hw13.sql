--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: adidas; Type: TABLE; Schema: public; Owner: vvk
--

CREATE TABLE public.adidas (
    id integer NOT NULL,
    name text,
    price integer NOT NULL
);


ALTER TABLE public.adidas OWNER TO vvk;

--
-- Name: adidas_id_seq; Type: SEQUENCE; Schema: public; Owner: vvk
--

CREATE SEQUENCE public.adidas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adidas_id_seq OWNER TO vvk;

--
-- Name: adidas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvk
--

ALTER SEQUENCE public.adidas_id_seq OWNED BY public.adidas.id;


--
-- Name: nike; Type: TABLE; Schema: public; Owner: vvk
--

CREATE TABLE public.nike (
    id integer NOT NULL,
    name text,
    price integer NOT NULL
);


ALTER TABLE public.nike OWNER TO vvk;

--
-- Name: nike_id_seq; Type: SEQUENCE; Schema: public; Owner: vvk
--

CREATE SEQUENCE public.nike_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.nike_id_seq OWNER TO vvk;

--
-- Name: nike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvk
--

ALTER SEQUENCE public.nike_id_seq OWNED BY public.nike.id;


--
-- Name: adidas id; Type: DEFAULT; Schema: public; Owner: vvk
--

ALTER TABLE ONLY public.adidas ALTER COLUMN id SET DEFAULT nextval('public.adidas_id_seq'::regclass);


--
-- Name: nike id; Type: DEFAULT; Schema: public; Owner: vvk
--

ALTER TABLE ONLY public.nike ALTER COLUMN id SET DEFAULT nextval('public.nike_id_seq'::regclass);


--
-- Data for Name: adidas; Type: TABLE DATA; Schema: public; Owner: vvk
--

COPY public.adidas (id, name, price) FROM stdin;
1	neo	23
2	smth1	44
\.


--
-- Data for Name: nike; Type: TABLE DATA; Schema: public; Owner: vvk
--

COPY public.nike (id, name, price) FROM stdin;
1	smthn	42
2	smthn1	43
3	smthn2	99
4	smthn3	78
\.


--
-- Name: adidas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vvk
--

SELECT pg_catalog.setval('public.adidas_id_seq', 2, true);


--
-- Name: nike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vvk
--

SELECT pg_catalog.setval('public.nike_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

