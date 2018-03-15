\subsubsection{What is the neuronal membrane made of}
The bulk of the membrane is composed of a 5nm thick lipid bilayer; Two layers of lipids which have their hydrophilic ends pointed outwards and their hydrophobic ends  pointed inwards.
\subsubsection{How thick is the neuronal membrane?}
About 5 nm
\subsubsection{What is meant by the resting membrane potential?}
The weighted average of the equilibrium potential of all the ions. $K^+$ higher concentration inside and diffuses easily through channels. The more K+ that goes outside membrane, the more negative the inside becomes, and the electrical potential increases untill it is big enough to counter the diffusion. Na+ has both consentration gradient and electrial gradient going inwards, but the channels are not as eager to let them through
\subsubsection{How big is typically the resting membrane potential?}
Around -60mV
\subsubsection{What are the key ions setting up the neuronal membrane potentia land mediating electrical signals?}
$Na^+, Ca^{2+}, K^+, Cl^-, OA^-$
\subsubsection{What is an ion channel?}
Ion chennels are pores in the lipid bilayer, made of proteins, which can allow ceratin ions to flow through the membrane
The membrane seperates the extracellular fluid from the cytoplasma. To let certain ions through the membrane have several ion channels, which can be leak channels; always open, but may only accept certain types of ions. They can be pumps, which f.eks pump out 3 Na+ ions in exchange for 2 K+ ions with the use of one ATP molecule.
We also have the active channels which are gated either by voltage or by ligands. Neurotransmitter reseptors may be ligand gated. The channels in the axons is mostly voltage gated, which help create the action potential.


\subsubsection{What are the two main categories of ion channels?}
Active and passive channels
\subsubsection{What is meant by an active channel?}
An active channel can exist in open or closed states, depending on e.g membrane potential, ionic concentrations or the presence of bound ligans, such as neurotransitters.
\subsubsection{What is meant by a passive channel?}
A passive channel does not change their permeability in responses to external influences
\subsubsection{What is an ion pump?}
An ion pump is an ion channel that pumps the ions in the "oposite direction" of where it want to go.

\subsubsection{Which ion pump is particularly important for setting up the resting membrane potential?}
When Na+ and K+ reaches equilibrium, there is no net flow of charge across the membrane, but there is net flow of Na+ and K+ and over time this would cause the consentrationgradient to run down.
\subsubsection{What is an electrogenic pump?}
The Na+K+ pump is electrogenic, beecause it changes the net charge in the cell by pumping out more positive particles than it pumps in. It seems like if the pump uses ATP this is a good indication of it being electrogenic.
\subsubsection{Describe the Nernst-Planck equation. What does it tell?}
This equation is a general description of how charged ions move in solution in electric fields. (Where they are influenced by electrical drift and diffusion)
\subsubsection{What is the Nernst potential?}
This is the equilibrium potential for one permeable ion.
$$E_X = \frac{RT}{z_X F}ln \frac{[X]_{out}}{[X]_{in}}$$
where $[X]_{out}$ and $[X]_{in}$ is ther intracellular and extracellular cocentrations of X
\subsubsection{Derive the Nernst potential from the Nernst-Planck equation.}
Consentration gradient:
$$J_{X, diff} = -D_X \frac{d[X]}{dx}$$
Where $D_X$ is the diffusion coefficient of molecule X\\
\\
Electrical drift:
$$J_{X, drift} = - \frac{D_X F}{RT} z_X [X] \frac{dV}{dx}$$
Where $z_X$ is the ion's signed valency (the charge of the ion measured as a mulitple of the elementary charge). R is the gas constant, T is the temperature in kelvins and F is faradys constant.\\
\\
Nerst-Planck:
$$J_X = -D_X \frac{d[X]}{dx} - \frac{D_X F}{RT} z_X [X] \frac{dV}{dx}$$
The Nernst equation is derived by assuming diffusion in one dimesion along a line that starts at x = 0 and ends at x = X. For there to be no flow of current (which is what the Nernst equation describes) the Nernst planck equation must be zero.\\
$$\frac{1}{[X]}\frac{d[X]}{dx} = - \frac{z_X F}{RT}\frac{dV}{dx}$$
$$\int_{E_m}^{0}-dV = \int_{[X]_{in}}^{[X]_{out}}\frac{RT}{z_X F[X]}$$
$$E_m = \frac{RT}{z_X F}ln \frac{[X]_{out}}{[X]_{in}}$$
\subsubsection{What is meant by the principle of electroneutrality?}
each atom in a stable substance has a charge close to zero
\subsubsection{Is a large deviation from electroneutrality needed to set up the resting membrane potential?}
From direct measurements the specific membrane capacitance is often set to be $1 \mu F cm^{-2} = 10^{-8} \mu F \mu m^{-2}$\\
If we consider the squid giant axion with diameter $500 \mu m$ and a section $1 \mu m$ long, with resting potential -70mV, we have
Area: $500 \times 1 \times \pi \mu m^2$\\
C: $500 \pi \times 10^{-8}\mu F$\\
Charge: $q = CV = 500 \pi \times 10^{-8}\mu F * 70 * 10^{-3} V = 35000\pi \times 10^{-11} \mu C$\\
Faradys constant: $F = 96485.3365 C/mol$ is the electrical charge of one mol of elektrons\\
Dividing by faradays: ...\\
volume: $\pi (500/2)^2 \mu m^3$ change to liters and multiply by 400 mM per liter. We get that there is almost 10 million times as many ions in the cytoplasm than on the membrane, and the effect of charging the membrane (releasing 1 part in 10 million, does not really matter. So we can assume electroneutrality. This ofcourse is different for a very small neuron.

\subsubsection{What does the Goldman-Hodgkin-Katz (GHK) model tell you?}
GHK predict the current $I_X$ mediated by a single ionic species X flowing across a membrane when the membrane potential is V.
\subsubsection{What approximations are assumed in the GHK model?}
\begin{itemize}
\item No current flows when the voltage is equal to the equilibrium potential. Electrical drift and diffusion is equal
\item the current changes direction at the equilibrium potential.
\item The idividual ions do not obey ohm's law since the current is not proportional to the voltage.
\item The potassium characteristic favours outward rectifying currents and the calcuim characteristic favours inward rectifying currents.
\end{itemize}
\newpage
\subsubsection{The GHK model can account for inward and outward rectification of ion currents. What is meant by this?}
Rectification is the property of allowing current to flow more freely in one direction than another. Potassiu favours outward current, and is described as outward rectifying. Calcium favours inward currents and is described as inward rectifying.
\subsubsection{In modeling one often assumes a quasi-ohmic relation between membrane potential and ion current. What is meant by quasi-ohmic?}
Making a linear approximation to th GHK equations is similar to assuming ohms law. Since the straight line does not necessearily pass through the origin, the correspondence is not exact and thid form om linear I-V relation is called quasi-ohmic.
\subsubsection{What is the capacitive current?}
Capacitive current is the description of how current affects the voltage across the membrane

\subsubsection{Derive/show a mathematical expression for it.}
Capacitance is defined as $q = CV$. The current flow through the membrane si $I = \frac{dq}{dt}$\\
We can differentiate:
$$I = \frac{dq}{dt} = C \frac{dV}{dt}$$
The change in voltage over time, dureing the charaging or discharging of the membrane, is inversley proportional to the capacitance.
\subsubsection{Derive a general expression for the reversal potential (Em) for a neuron with several quasi-ohmic ion channels.}
????
\subsubsection{Derive a differential equation for a simple RC-circuit neuron.}
??
\subsubsection{Show that the solution for the membrane potential V for this RC-circuit neuron receiving a constant step current at time t = 0 is given by V (t) = A + B(1 - exp(-t/C)). Determine the constants A, B, and C.}
??
\subsubsection{What is the limiting value of V when $t \rightarrow \infty$}
..
\subsubsection{At time te the current is turned off. Show that the solution for the membrane potential V for the RC-circuit neuron receiving after time te is given by V (t) = A' + B' exp(-(t - te)/C')). Determine the constants A', B', and C'.}
..
\subsubsection{What is the membrane time constant $\tau_m$?}
..
\subsubsection{What is the input resistance?}
Input resistance is defined as the change in the steady state membrane potential divided by the injected current causing it.
To determine the input resistance, the resting membrane potential is first measured. Then a small amout of current $I_e$ is injected and the membrane potential is allowed to reach a steady state $V_{\infty}$. The input resistance is then given by.
$$R_{in} = \frac{V_{\infty} - E_m}{I_e}$$
