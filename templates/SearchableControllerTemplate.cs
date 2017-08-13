using Common.Controllers;
using Common.Model.<#package#>;
using Persistence<#package#>;

namespace <#package#>.Controllers
{
    public class <#name#>Controller : SearchableController<<#name#>, <#name#>.SortBy, <#name#>.FilterAttribute>,
        I<#name#>Controller
    {
        public <#name#>Controller(I<#name#>Repository repository) : base(repository)
        {
        }
    }
}