# Efficient Collective Action for Tackling Time-Critical Cybersecurity Threats

written by Sébastien Gillard, Dimitri Percia David, Alain Mermoud and Thomas Maillart

# Abstract
The latency reduction between the discovery of vulnerabilities, the build-up and dissemination of cyber-attacks has put
significant pressure on cybersecurity professionals. For that, security researchers have increasingly resorted to collective
action in order to reduce the time needed to characterize and tame outstanding threats. Here, we investigate how joining
and contributions dynamics on MISP, an open source threat intelligence sharing platform, influence the time needed
to collectively complete threat descriptions. We find that performance, defined as the capacity to characterize quickly a
threat event, is influenced by (i) its own complexity (negatively), by (ii) collective action (positively), and by (iii) learning,
information integration and modularity (positively). Our results inform on how collective action can be organized at scale
and in a modular way to overcome a large number of time-critical tasks, such as cybersecurity threats.

Link: https://arxiv.org/abs/2206.15055

Code:
- MISP_data_retrieving.py: allows to retrieve MISP data from the RestAPI. To do that, we have to request an access to MISP CIRCL
- MISP_export_to_csv.ipynb: transform the .json files into different .csv
- Figures.ipynb: generate the figures illustrating the paper
- Econometric_Model.ipynb: provide the results of the multivariate cross-sectional regression
- Figures: Folder with the figures created by igures.ipynb
