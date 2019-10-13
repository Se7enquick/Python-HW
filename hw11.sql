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
-- Name: actors; Type: TABLE; Schema: public; Owner: vvk
--

CREATE TABLE public.actors (
    actor text,
    film text
);


ALTER TABLE public.actors OWNER TO vvk;

--
-- Name: films; Type: TABLE; Schema: public; Owner: vvk
--

CREATE TABLE public.films (
    film text,
    producer text,
    actor text
);


ALTER TABLE public.films OWNER TO vvk;

--
-- Name: producers; Type: TABLE; Schema: public; Owner: vvk
--

CREATE TABLE public.producers (
    producer text,
    film text
);


ALTER TABLE public.producers OWNER TO vvk;

--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: vvk
--

COPY public.actors (actor, film) FROM stdin;
Johnny Depp	\N
\N	Chocoalte Factory(2005)
Robert Downey JR	\N
\N	Iron Man
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: vvk
--

COPY public.films (film, producer, actor) FROM stdin;
\.


--
-- Data for Name: producers; Type: TABLE DATA; Schema: public; Owner: vvk
--

COPY public.producers (producer, film) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

