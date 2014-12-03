---
title: Web technologies update
layout: post
description: "It's been a long time since I javascript"
author: absorto
---

Data analysis tools which I work on these days are better brought to the web through meta-applications like [Galaxy](http://galaxyproject.org). Although complex pipelines are best just scripted and shared through a software repo.

Anyway, I'm involved in the development of a web app again. In the process of [looking before leaping](http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003506) I found [this anouncement](http://yahooeng.tumblr.com/post/96098168666/important-announcement-regarding-yui) about an entire library being deprecated. Made me realize it's been a long time since I've done any serious web development. Not that I ever used YUI, but it seems I missed an entire transition phase which has landed us in Javascript, which I'm not too enthusiastic about.

Oh well. I loked around and found [w2ui](http://w2ui.com/web/) which seems easy enough.

However I do like those RESTful interfaces.

So on the side of the server my plan is to move away from [Django](http://djangoproject.com). The best part of it is the ORM, but I don't think I'll need the OO abstraction to represent documents which I plan to store on [mongoDB](http://mongodb.org). So: [Flask](http://flask.pocoo.org) here I come, and later I'll probably attempt a rewrite in [ring](https://github.com/ring-clojure/ring/wiki/Getting-Started) just for fun.

Kids these days!
