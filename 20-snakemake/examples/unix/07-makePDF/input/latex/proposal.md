---
    title: "Deserving a Treat: Public Good Provision and Corruption"
    author: "Ulrich Bergmann & Aurelia Buchs"
    date: "10/06/2017"
    header-includes:
        \usepackage[utf8]{inputenc}
        \usepackage{natbib}
        \usepackage{graphicx}
        \usepackage{setspace,parskip}
        \usepackage{pdflscape}
        \usepackage{afterpage}
        \usepackage{booktabs}
        \usepackage{capt-of}
        \usepackage{subcaption}
        \newtheorem{prediction}{Prediction}
---


\section{Introduction}
It is well document how bad corruption is for a society. \citeauthor{Mauro1995Corruption}'s (\citeyear{Mauro1995Corruption}) seminal paper started the empirical literature and shows that corruption leads to a decrease in private investment and lower economic growth\footnote{The robustness of his results have been called into question lately, for example by \citet{Svensson2005Eight}.}. \citet{Dreher2005Economic} estimate that an increase in corruption by about one index point reduces GDP growth by 0.13\% and annual GDP per capita by \$425. \citet{Bandiera2009Active} estimate that corruption might cost the Italian government up to 2\% of GDP anually in inflated procurement costs alone.

While political corruption is often associated with autocratic and developing countries \citep{Serra2006Empirical}, the recent affairs surrounding then Korean president Park Gun-hye and François Fillon, the republican candidate to the French presidency in the 2017 election, remind us that corruption is also a problem in western and democratic societies. It has been shown that democratic institutions have a negative impact on the aggregate level of corruption in a country \citep{Serra2006Empirical} but is it possible that the same institution psychologically motivate corruption in democratic politicians on an individual level? Is it possible that established politicians feel more entitled to private gains as a consequence of their service to the public which defines the role of a democratically elected official?

We hypothesize that subjects who act selflessly and supply a public good, feel more entitled to asymmetrically receive private rewards in comparison to the public. Our mechanism is able to explain corruptive behavior in decorated public servants and politicians and adds a new channel to explain high-profile corruption that goes beyond the common place idea that rationalizes these cases through lack of monitoring for officials that are higher up the chain. The second channel thereby allows us to shed more light on the riddle of why high-profile corruption exists in spite of the substantially higher costs of detection for decorated officials.

Our paper contributes to the growing experimental literature on corruption. We follow the main insight from \citet{Banerjee2016On} that subjects engage in corruptive practices if they feel entitled to additional private gains. We show that acting socially and serving the public can trigger such a feeling of entitlement and hence lead to more corrupt tendencies.

In this paper we propose an abstract experimental setup to test the entitlement hypothesis. Our design combines a public good game and the dice task introduced by \citet{Fischbacher2013Lies} to investigate the causal effect of contributions to a public good on the propensity to cheat for private gains.
Our experimental design is novel and contrasts with the standing experimental literature on corruption which features numerous variations of the bribery game\footnote{The game involves three parties. A citizen can offer a bribe to an official. If the bribe is accepted, the citizen receives public funds causing a negative externalities on a third party.} which was introduced by Frank and Schulze (200) and formalized by \citet{Abbink2002Experimental}. The game has been used to investigate inter-alia the influence of institutional, social and cultural factors on corruption \citep{Banerjee2016On}

The remainder of the article is organized as follows. Section 2 describes the experimental design used. Section 3 presents predictions following the entitlement hypothesis and the theory of type-based-altruism. Section 4 presents the summary statistics and the main experimental results. Finally, Section 4 concludes.

\section{Experimental Design}
We recruited 24 subjects from the populations of experimental participants at the University of Zurich. The experiment was carried out on the computers of the laboratory for experimental and behavioral economics at the University of Zurich using zTree \citep{Fischbacher2007ZTree}. The Participants received 18 CHF upon arrivals which they could invest in the \emph{first stage} of the experiment which featured a public good game.

\subsection*{Stage 1: Public Good Game}
The subjects were anonymously divided into groups with four subjects each. They could invest $x \in [0,18]$ CHF into a social project that was shared among the four group members. For each unit invested by a single member, each member of the group received $0.4$ units of money. This implies that each  unit invested increase the total sum of payoff in the group by $4\times 0.4 - 1 = 0.6$ monetary units. This defines the payoff of group member $i$ as $\pi_i = 18 - x_i + \sum_{j \in \mathit{group}} x_j$. Because the multiplicator $0.4<1$ it was individually rational to contribute $x^*=0$ units. As $4\times 0.4 =1.6>1$ the social welfare was maximized with a contribution of $x^{**}=18$ by all group members. The contradicting motives generate a natural variation in contribution. The first stage is therefore designed to vary the entitlement that subjects feel through the variation in their relative contribution compared to their group members. To maximize the variation in entitlement, each subject was presented with a feedback screen which features the average contribution of all members of a group and the individual contribution of the respective subject (See \textbf{FIGURE X} in Appendix B).

\subsection*{Stage 2: Dice Task}
The \emph{second stage} then featured the dice task introduced by \citet{Fischbacher2013Lies}. Subjects received a physical six-sided dice and were asked to privately roll it and to report the thrown number $\in \{1,2,3,4,5,6\}$ into an input box on the computer screen. We made clear that the dice roll was completely private and unobserved both by other subjects nor the experimenters. Additionally, we supplied the subjects with an opaque plastic cup (See Appendix C) that subjects were instructed to use for the dice roll and have a private peak to make the privacy of the dice roll even more salient.

A subject's payoff in stage 2 was equal to the thrown number in CHF. It was therefore payoff maximizing for each subject to report that the number six was thrown. A subjects total payoff is equal to the sum of Stage 1 and Stage 2 payoffs.

%The proposed design tries to test the entitlement hypothesis in the simplest way possible. We therefore design a first stage that is meant to maximize entitlement through warm glow altruism and a second stage that measures if the feeling of entitlement causes subjects to cheat and internalize more resources compared to a fair share.

The full paper based instructions to the experiment and stage 1 can be found in Appendix A. Appendix B features all screens of the experiment. A photo of the plastic cup is featured in Appendix C.

\section{Predictions}

The entitlement hypothesis predicts that subjects who behave more pro-socially at individual costs in Stage 1, feel more entitled to a higher payoff than their peers. Following \citet{Banerjee2016On} we should consequently observe an increase in corrupt behavior which we identify in upward-biased reported thrown numbers in the dice task of Stage 2. Stage 1 allows for two interpretations of pro-social behavior. Firstly, subjects may feel more entitlement as a positive to their absolute contribution to the group project. Prediction 1 formalizes this claim.

\begin{prediction}[Absolute Entitlement]
    Subjects with higher contributions in Stage 1, report on average a higher thrown dice number in Stage 2.
\end{prediction}


Secondly, subject may evaluate their private contribution relative to that of the other group members. This interpretation implies that those subjects, who contributed more than the group average to the group project, should feel systematically more entitled than their peers, who contributed less than the group average to the group project.

\begin{prediction}[Relative Entitlement]
    Subjects with above average contributions in Stage 1, report on average a higher thrown dice number in Stage 2.
\end{prediction}

This prediction stands in clear contrast to type-based models of social preferences like the one proposed by Levine (1998). In these models each subject is characterized by a fixed parameter that describes her level of altruism. A subject with a higher level of altruism will act more pro-socially compared to a less altruistic person irrespective of the environment. This classic interpretation therefore predicts that those subjects who act as more altruistic in stage 1 also act more altruistic in stage 2 towards the experimenter and, consequently, lie less.

\begin{prediction}[Type-based social preferences]
Subjects who share more in Stage 1, report on average a lower thrown dice number in Stage 2.
\end{prediction}

\section{Results}
In this section we first present descriptive statistics of the distribution of the main independent and dependant variables from Stage 1 and Stage 2 respetively. Afterwards, we present our main results in form of an OLS-regression. The small sample size of this trial run makes it difficult to make proper statistical inference and the results have to be taken with caution. Anyhow, we believe the results yield a first hint that seems to confirm Prediction 2.

\subsection{Summary Statistics}

A total of 24 participants took part in the experimental session. Figure 1 (a) shows the resulting distribution of the contributions to the social project in Stage 1 and Figure 1 (b) the distribution of the reported dice throws from the dice task of Stage 2.

\begin{figure}[!h]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=\linewidth]{output/graphs/first-stage.png}
  \caption*{\footnotesize (a) Frequencies of Stage 1 contributions.}
  \label{fig:sub1}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=\linewidth]{output/graphs/second-stage.png}
  \caption*{\footnotesize (b) Frequencies of Stage 2 dice throw.}
  \label{fig:sub2}
\end{subfigure}
\caption*{\footnotesize Figure 1: Frequencies of subjects' actions in (a) Stage 1 and (b) Stage 2 (Stars show significant deviations from the expected frequency of 16.67\% under a uniform distribution in Stage 2 (*=10\%-level, **=5\%-level, ***=1\%-level).}
\end{figure}

Both graphs clearly suggest that the distribution in both stages differ significantly from a uniform distribution. A Kolmogorov-Smirnov one sample test confirms this for the dice throw at the 1\%-level. We see in Panel (a) that Stage 1 contributions are biased downwards. 12 subjects choose a contribution level of less than half of the original endowment of 18 with 17\% choosing the individually rational contribution level of 0. Interestingly, 20\% of our sample act completely in accordance with the welfare maximizing contribution level and contribute their full endowment. Panel (b) shows that reported dice throws are biased upwards. In fact we observe the expected frequency for both the numbers 3 and 4 but observe that no subject reports to have thrown a 2. Only a single subject reports to have thrown the number 1. This subject was also one of the subjects who contributed his or her full endowment in Stage 1 and therefore acts completely social in Stage 1 and completely (with a very high likelyhood) honest in Stage 2. This subject also received one of the lowest overall payoffs (13.8 CHF) in our experiment which is considerably less than half of the payoff of other participants. Because of the small sample size we will in some test exclude this subject as an outlier because he or she has a very large effect on the estimated results. The systematic shift of reported numbers 1 and 2 towards numbers 5 and 6 suggests that the subject pool believe in the privacy of the dice throw and that they also understand the payment structure of Stage 2.


\subsection{Main Results}

To test Prediction 2, we divide the subjects into two sub-pools -- those who contributed more than the average and less than the average in their respective groups. The feedback screen made subjects aware of the fact that their contribution was below or above the average one in their group. We can therefore treat these groups as two different endogenous treatment groups. As most subjects chose a low contribution level in Stage 1, the \emph{BELOW\_AVERAGE} treatment groups (N=16) includes more subjects than the \emph{ABOVE\_AVERAGE} treatment group (N=8).



\begin{figure}[!h]
\centering
\includegraphics[width=0.7\textwidth]{output/graphs/boxplot.png}
\caption*{\footnotesize Figure 2: Box-plot of reported dice throw in Stage 2 for subjects with below or above average contributions in Stage 1.}

\vspace*{.5cm}
\begin{tabular}{lllllll}
\toprule
Treatment      & \multicolumn{6}{c}{Reported Dice Thrown (in \%)} \\
                        & 1       & 2     & 3       & 4     & 5         & 6 \\
                        \midrule
Below Average (16)   & 0*      & 0*    & 18.8    & 25    & 43.8**    & 12.5      \\
Above Average (8) & 12.5    & 0     & 12.5    & 0     & 12.5      & 62.5*** \\
\bottomrule
\end{tabular}
\caption*{\footnotesize Table 1: Binomial test for uniform distribution of reported dice throw in Stage 2 for subjects with below or above average contributions in Stage 1. The stars show significant deviations from the expected frequency of 16.67\% under a uniform distribution (*=10\%-level,**=5\%-level,***=1\%-level).}
\end{figure}

Figure 2 shows box-plots of the reported dice throws for both. The graphic suggests to confirm Prediction 2 as the more entitled \emph{ABOVE\_AVERAGE} treatment groups seems to report a systematically higher dice throw than the \emph{BELOW\_AVERAGE} one in Stage 2. A median test supports this at a significant difference at the 5 \%-level (Pr=0.039), confirming that the median of the reported dice throw is significantly higher in the \emph{ABOVE\_AVERAGE} group. Table 1 shows that the modus of the distribution of reported dice throws is in fact the highest possible number 6 for the \emph{ABOVE\_AVERAGE} group with almost two-thirds of the subjects reporting a perfect dice throw. The modus of the \emph{BELOW\_AVERAGE} group is shifted slightly downwards with more than 40\% of the subjects reporting a dice throw of 5. We believe that this table 1 shows most clearly the presence of the entitlement effect in our experiment. A Wilcoxon-Mann-Whitney ranksum test for equality of distributions, however, reveals no significant difference between the reported dice throw in the two groups ($Pr(\>\|z\|)$ = 0.1442; n=24, ABOVE\_AVERAGE=8, BELOW\_AVERAGE=16) for our small sample size.


Table 1 presents our results from the OLS-regression. In the first column we regress the reported dice throw on the Stage 1 contribution alone. The result is not significantly different from 0. In the second column we regress the reported payoffs on a dummy variable which takes the value 1 for subjects in the \emph{ABOVE\_AVERAGE} groups and a value of 0 for members of the \emph{BELOW\_AVERAGE} group. Again the result is not significantly different from 0. If we exclude the only subject who reported a dice throw below 3, we see in Column (3) that the coefficient for the Stage 1 contribution switches its sign but stays insignificant. In Column (4), however, we already get weak significance for the \emph{ABOVE\_AVERAGE} dummy variable even for our extremely small sample size. Subjects who contributed above their group average in stage 1 reported a 0.929 higher dice throw than subjects below average (which confirms the visual impression from Table 1). By excluding the outlier we also manage to get rid of the heteroskedacity.   In column 6, 7 and 8 we additionally included some additional control variables which all yield non-significant coefficients. The variables are respectively the earned individual profit in Stage 1, the time the subjects spent looking at the screen that compared their respective contribution to the group average and an interaction term between group membership and the time spent looking at the screen revealing this information. The idea to include the last interaction term is was to reduce the effect of subjects who did not look at the feedback screen long enough to internalize a feeling of entitlement. Yet, the interaction terms is not significant which might be, however, only an artifact of the small sample size. In terms of explained variance we can see  on the R-squared values that our models at best are able to explain roughly about 20 percent of the variance.
However, we have to remind the reader that the OLS-results have to be taken with extreme caution as we have a highly skewed dependent variable which is not continuous but discrete with only 6 values.

\section{Conclusion}
In our laboratory experiment we test the assumption that corruption might not only be the result of the institutional context but also have its roots in psychological motives at the individual level. To investigate this, we combine a public good game in the first stage and a dice rolling task in the second stage.
Our pilot study hints that pro-social behavior for the common good can generate a feeling of entitlement in the individual which induces dishonest and purely selfish behavior, a behavior similar to corruptive practices.

 Of course our pilot study needs to replicated with a bigger sample size in order to get clearer evidence on this question. The preliminary results do, however, suggest that this endeavor promises to be of value. A big advantage of our experiment is that the dice rolling task could easily be added to any ordinary public good game or other study that features social behavior which might make further data generation easy and cheap.

\bibliographystyle{aea}
\bibliography{input/latex/Remote.bib}

\afterpage{%
   % \clearpage% Flush earlier floats (otherwise order might not be correct)
    \thispagestyle{empty}% empty page style
    \begin{landscape}% Landscape page
        \centering % Center table

        \input{output/tables/ols-regression.tex}

        \captionof*{table}{\footnotesize Table 2: OLS-Regression for reported payoffs in second stage (SE in parentheses, *$p<0.1$, **$p<0.05$, ***$p<0.01$)}% Add 'table' caption
      \end{landscape}
      \clearpage% Flush page
  }