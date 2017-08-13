using Common.Controllers;
using Common.Model.<#package#>;

namespace <#package#>
{
    public interface I<#name#>Controller : ISearchableController<<#name#>, <#name#>.SortBy, <#name#>.FilterAttribute>
    {
    }
}